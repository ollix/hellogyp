{
  'includes': [
    '../common.gypi'
  ],
  'targets': [
    {
      'target_name': 'HelloGYP',
      'product_name': 'HelloGYP',
      'type': 'executable',
      'production_extension': 'bundle',
      'mac_bundle': 1,
      'dependencies': [ '../hellogyp/hellogyp.gyp:hellogyp' ],
      'sources': [
        'HGAppDelegate.mm',
        'HGRootViewController.mm',
        'main.mm',
      ],
      'mac_bundle_resources': [
        'English.lproj/InfoPlist.strings',
      ],
      'link_settings': {
        'libraries': [
          '$(SDKROOT)/System/Library/Frameworks/Foundation.framework',
          '$(SDKROOT)/System/Library/Frameworks/UIKit.framework',
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
