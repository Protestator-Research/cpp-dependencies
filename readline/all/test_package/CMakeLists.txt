cmake_minimum_required(VERSION 3.15)
project(test_package C)

find_package(readline CONFIG REQUIRED)

# readline 8.2 declares rl_message() without parameters, which means "no arguments" in C23
set(CMAKE_C_STANDARD 17)

add_executable(${PROJECT_NAME} test_package.c)
target_link_libraries(${PROJECT_NAME} readline::readline)
