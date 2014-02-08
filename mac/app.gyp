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
				'INFOPLIST_FILE': 'HelloGyp-Info.plist',
				'OTHER_CFLAGS': [
					'-std=c++11',  # supports C++11
				],
			},  # xcode_settings
		}
	]
}
