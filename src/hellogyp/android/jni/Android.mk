LOCAL_PATH := $(call my-dir)

# Includes dependent makefiles.
include $(LOCAL_PATH)/../../../GypAndroid.mk

include $(CLEAR_VARS)

LOCAL_MODULE := hello-jni

LOCAL_STATIC_LIBRARIES := hellogyp

LOCAL_SRC_FILES := hellogyp/android/jni/hello_jni.c

include $(BUILD_SHARED_LIBRARY)

