gyp --depth=../ -f android ../hellogyp/hellogyp.gyp
ndk-build
ant debug install
adb shell am start -a android.intent.action.MAIN \
                   -n com.example.hellogyp/com.example.hellogyp.MainActivity
