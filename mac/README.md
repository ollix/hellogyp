This example shows how to use GYP to create a Mac app with C++ library support.

Generate the Xcode project

		gyp app.gyp --depth=. -f xcode

Build the app by `xcodebuild`...

		xcodebuild -project app.xcodeproj/ -target HelloGYP

Or using `xctool`...

		xctool -project app.xcodeproj/ -scheme HelloGYP

You can also use `ninja` to build the app...

	gyp app.gyp --depth=. -f ninja
	ninja -C out/Debug/
