cmake_minimum_required(VERSION 3.1)
project(test_package C)

find_package(nss)

add_executable(${PROJECT_NAME} test_package.c)
target_include_directories(${PROJECT_NAME} PUBLIC ${nss_INCLUDE_DIRS} ${nspr_INCLUDE_DIRS})
target_link_libraries(${PROJECT_NAME} nss::nss nspr::nspr)


