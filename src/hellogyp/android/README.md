Install requirements on Mac
```
brew install android-sdk android-ndk ant
```

This directory is created by the android tool on the command line and was
executed at its parent's directory.
```
android create project -n HelloGYP -t android-19 -p android -a MainActivity -k com.example.hellogyp
```

Build the app
```
ant debug
```

Open the AVD Manager and launch a virtual device
```
android avd
```

Install the app to emulator
```
adb install bin/HelloGYP-debug.apk
```
