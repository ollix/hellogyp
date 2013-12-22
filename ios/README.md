This example shows how to use GYP to create an iOS app with C++ library support.

Generate the Xcode project

    gyp app.gyp --depth=. -DOS=ios

Build the app by `xcodebuild`...

    xcodebuild -project app.xcodeproj/ -target HelloGYP -configuration Debug -sdk iphonesimulator build

Or using `xctool`...

    xctool -project app.xcodeproj/ -scheme HelloGYP -configuration Debug -sdk iphonesimulator build
