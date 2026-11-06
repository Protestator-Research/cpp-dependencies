#!/usr/bin/env python3
"""Select the CI jobs that have to run for the changes between two commits.

A job is selected when one of these is true:
  * its recipe folder changed,
  * a folder of a direct or transitive dependency changed (from the requirements
    in conanfile.py, followed through recipes that have no CI job of their own),
  * its own definition in the workflow changed (e.g. a version was added),
  * a job it `needs` is selected.

Everything is selected when no usable base commit exists (manual run, new branch,
force push), because the changes cannot be determined then.

The result is written as a JSON array to the `jobs` output of the step.
"""
import ast
import json
import os
import re
import subprocess
import sys
import warnings
from pathlib import Path

import yaml

# Some recipes contain invalid escape sequences; that is irrelevant for reading their requirements.
warnings.simplefilter("ignore", SyntaxWarning)

WORKFLOW = ".github/workflows/c-cpp.yml"
THIS_JOB = "detect-changes"
RECIPE_PATH = re.compile(r"conan\s+create\s+\./([^/\s]+)")
REQUIREMENT = re.compile(r"([A-Za-z0-9_.+-]+)/")
REQUIRE_NAMES = {"requires", "tool_requires", "build_requires", "test_requires", "python_requires"}


def git(*args):
    return subprocess.run(["git", *args], check=True, capture_output=True, text=True).stdout


def needs_of(job):
    needs = job.get("needs") or []
    return [needs] if isinstance(needs, str) else list(needs)


def recipe_folder(job):
    for step in job["steps"]:
        match = RECIPE_PATH.search(step.get("run") or "")
        if match:
            return match.group(1)
    return None


def build_definition(job):
    """The parts of a job that decide what it builds; `needs` and `if` only control scheduling."""
    return job.get("runs-on"), job.get("env"), job.get("steps")


def strings_in(node):
    """All string literals below an AST node, including the leading text of f-strings."""
    for child in ast.walk(node):
        if isinstance(child, ast.Constant) and isinstance(child.value, str):
            yield child.value


def direct_requirements(folder):
    """Names of all recipes that any conanfile of a recipe folder can require."""
    found = set()
    conanfiles = [*Path(folder).glob("conanfile.py"), *Path(folder).glob("*/conanfile.py")]
    for conanfile in conanfiles:
        for node in ast.walk(ast.parse(conanfile.read_text(errors="replace"))):
            value = None
            if (
                isinstance(node, ast.Call)
                and isinstance(node.func, ast.Attribute)
                and node.func.attr in REQUIRE_NAMES
            ):
                value = node
            elif isinstance(node, ast.Assign) and any(
                isinstance(target, ast.Name) and target.id in REQUIRE_NAMES for target in node.targets
            ):
                value = node.value
            if value is not None:
                for text in strings_in(value):
                    match = REQUIREMENT.match(text)
                    if match:
                        found.add(match.group(1))
    return found - {folder}


def folder_closure(folder, cache):
    """The folder itself plus all folders it transitively requires."""
    seen = set()
    stack = [folder]
    while stack:
        current = stack.pop()
        if current in seen or not Path(current).is_dir():
            continue
        seen.add(current)
        if current not in cache:
            cache[current] = direct_requirements(current)
        stack.extend(cache[current])
    return seen


def select(jobs, base_jobs, changed_folders):
    cache = {}
    selected = set()
    for name, job in jobs.items():
        folder = recipe_folder(job)
        if folder and folder_closure(folder, cache) & changed_folders:
            selected.add(name)
        elif name not in base_jobs or build_definition(job) != build_definition(base_jobs[name]):
            selected.add(name)

    # A selected job makes everything that needs it selected as well.
    changed = True
    while changed:
        changed = False
        for name, job in jobs.items():
            if name not in selected and selected.intersection(needs_of(job)):
                selected.add(name)
                changed = True
    return selected


def resolve_base(base):
    """Return a usable base commit, or None when everything has to be built."""
    if not base or not base.strip("0"):
        return None
    try:
        git("cat-file", "-e", f"{base}^{{commit}}")
    except subprocess.CalledProcessError:
        return None
    return base


def main():
    jobs = yaml.safe_load(Path(WORKFLOW).read_text())["jobs"]
    jobs = {name: job for name, job in jobs.items() if name != THIS_JOB}

    base = resolve_base(os.environ.get("BASE_SHA", ""))
    if base is None:
        print("No usable base commit, selecting all jobs.")
        selected = set(jobs)
        changed_folders = set()
    else:
        paths = git("diff", "--name-only", "--no-renames", base, "HEAD").splitlines()
        changed_folders = {path.split("/", 1)[0] for path in paths if "/" in path}
        base_jobs = yaml.safe_load(git("show", f"{base}:{WORKFLOW}"))["jobs"]
        selected = select(jobs, base_jobs, changed_folders)

    ordered = [name for name in jobs if name in selected]
    print(f"Changed folders: {sorted(changed_folders)}")
    print(f"Selected {len(ordered)} of {len(jobs)} jobs:")
    print("\n".join(f"  {name}" for name in ordered))

    output = os.environ.get("GITHUB_OUTPUT")
    if output:
        with open(output, "a") as handle:
            handle.write(f"jobs={json.dumps(ordered)}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
