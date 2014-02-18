export ANDROID_BUILD_TOP=`pwd`/../
gyp --depth=../ -f android jni/jni.gyp
ndk-build
ant debug install
adb shell am start -a android.intent.action.MAIN \
                   -n com.example.hellogyp/com.example.hellogyp.MainActivity
