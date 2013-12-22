LOCAL_PATH := $(call my-dir)

# Includes dependent makefiles.
include $(LOCAL_PATH)/../../../GypAndroid.mk

include $(CLEAR_VARS)

LOCAL_MODULE := hello-jni

LOCAL_STATIC_LIBRARIES := hellogyp_hellogyp_gyp

LOCAL_DEFAULT_CPP_EXTENSION := .cc

LOCAL_SRC_FILES := hellogyp/android/jni/hello_jni.cc

include $(BUILD_SHARED_LIBRARY)
