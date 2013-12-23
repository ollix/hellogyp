{
  'conditions': [
    ['OS=="ios"', {
      'xcode_settings': {
        'SDKROOT': 'iphoneos',
      },  # xcode_settings
    }],  # OS=="ios"
    ['OS=="mac" and "<(GENERATOR)"=="ninja"', {
      'make_global_settings': [
        ['CC', '/usr/bin/clang'],
        ['CXX', '/usr/bin/clang++'],
      ],
    }],  # OS=="mac" and "<(GENERATOR)"=="win"
  ],  # conditions
  'target_defaults': {
    'default_configuration': 'Debug',
    'configurations': {
      'Debug': {
        'cflags': [
          '-g',
          '-O0',
        ],
        'defines': [
          'DEBUG',
        ],
      },
      'Release': {
        'cflags': [
          '-Os',
        ],
        'defines': [
          'NDEBUG',
        ],
      }
    },
    'conditions': [
      ['OS=="ios"', {
        'xcode_settings': {
          'TARGETED_DEVICE_FAMILY': '1,2',
          'CODE_SIGN_IDENTITY': 'iPhone Developer',
          'IPHONEOS_DEPLOYMENT_TARGET': '7.0',
          'ARCHS': '$(ARCHS_STANDARD)',
        },
      }],  # OS=="ios"
    ],  # conditions
  },
}
