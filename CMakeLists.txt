cmake_minimum_required(VERSION 3.26)
project(TestModule)

add_library(custom SHARED custom.c)

if (WIN32)
	set_target_properties(custom PROPERTIES SUFFIX ".pyd")
endif()

target_include_directories(custom PRIVATE "D:/Program Files/Python312/Lib/site-packages/numpy/core/include/numpy")
target_include_directories(custom PRIVATE "D:/Program Files/Python312/include")
target_link_directories(custom PRIVATE "D:/Program Files/Python312/libs")

add_custom_command(TARGET custom POST_BUILD
	COMMAND cmd /c "stubgen -m custom -o ./"
	WORKING_DIRECTORY $<TARGET_FILE_DIR:custom>
)