cmake_minimum_required(VERSION 3.28)
project(icpc)

set(CMAKE_CXX_STANDARD 14)

include_directories(2023/3)
include_directories(2023/9)
include_directories(2023/11)
set(SOURCE_FILES 2023/3/main.cpp 2023/9/main.cpp 2023/11/main.cpp)

add_executable(2023-3 2023/3/main.cpp)
add_executable(2023-9 2023/9/main.cpp)
add_executable(2023-11 2023/11/main.cpp)
