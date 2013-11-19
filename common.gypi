{
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
    'include_dirs': [
      'src',
    ],
  },
}
