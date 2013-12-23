{
	'includes': [
		'../common.gypi'
	],
	'targets': [
		{
			'target_name': 'HelloGYP',
			'product_name': 'HelloGYP',
			'type': 'executable',
			'mac_bundle': 1,
			'dependencies': [ '../hellogyp/hellogyp.gyp:hellogyp' ],
			'sources': [
				'HGAppDelegate.mm',
				'main.mm',
			],
			'include_dirs': [
				'..',
			],
			'mac_bundle_resources': [
				'English.lproj/Credits.rtf',
				'English.lproj/InfoPlist.strings',
				'English.lproj/MainMenu.xib',
				'Images.xcassets',
			],
			'link_settings': {
				'libraries': [
					'$(SDKROOT)/System/Library/Frameworks/Cocoa.framework',
				],
			},
			'xcode_settings': {
				'OTHER_CFLAGS': [
					'-std=c++11',
				],
				'INFOPLIST_FILE': 'HelloGyp-Info.plist',
				'SDKROOT': 'macosx',  # -isysroot
				'CONFIGURATION_BUILD_DIR': 'build/Default',
				'CLANG_ENABLE_OBJC_ARC': 'YES',
			},

		}
	]
}
