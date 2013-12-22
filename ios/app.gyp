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
      'sources': [
        'HGAppDelegate.mm',
        'HGRootViewController.mm',
        'main.mm',
      ],
      'include_dirs': [
        '..',
      ],
      'mac_bundle_resouces': [
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
        'SDKROOT': 'iphoneos',  # -isysroot
        'IPHONEOS_DEPLOYMENT_TARGET': '7.0',
        'CONFIGURATION_BUILD_DIR': 'build/Default',
        'CLANG_ENABLE_OBJC_ARC': 'YES',
      },
      'dependencies': [
        '../hellogyp/hellogyp.gyp:hellogyp'
      ],
    }
  ]
}
