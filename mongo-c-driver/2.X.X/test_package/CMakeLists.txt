cmake_minimum_required(VERSION 3.15)
project(test_package LANGUAGES C)

find_package(mongoc REQUIRED CONFIG)

add_executable(${PROJECT_NAME} test_package.c)
if(TARGET mongoc::mongoc_shared)
    target_link_libraries(${PROJECT_NAME} PRIVATE mongoc::mongoc_shared mongoc::bson_shared)
else()
    target_link_libraries(${PROJECT_NAME} PRIVATE mongoc::mongoc_static mongoc::bson_static)
endif()
