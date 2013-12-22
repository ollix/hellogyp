# use this to select gcc instead of clang
# NDK_TOOLCHAIN_VERSION := 4.8
# otherwise, the following line select the latest clang version.
NDK_TOOLCHAIN_VERSION := clang
# enable c++11 extentions in source code
APP_CPPFLAGS += -std=c++11
# or use APP_CPPFLAGS := -std=gnu++11
# Following is STL implementation. Can be use _static or _shared version, the
# last one need a call to loadLibrary BEFORE use the C++ code in the shared
# library
APP_STL := gnustl_static
