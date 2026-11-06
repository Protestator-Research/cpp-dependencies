script_folder="/home/herzog/Dokumente/Projekte/cpp-dependencies/cmake/binary/test_package"
echo "echo Restoring environment" > "$script_folder/deactivate_conanrunenv-release-x86_64.sh"
for v in PATH
do
   is_defined="true"
   value=$(printenv $v) || is_defined="" || true
   if [ -n "$value" ] || [ -n "$is_defined" ]
   then
       echo export "$v='$value'" >> "$script_folder/deactivate_conanrunenv-release-x86_64.sh"
   else
       echo unset $v >> "$script_folder/deactivate_conanrunenv-release-x86_64.sh"
   fi
done

export PATH="/tmp/claude-1000/conan3/p/b/cmake18e3436467688/p/bin${PATH:+:$PATH}"