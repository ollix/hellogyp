{
  'includes': [
    '../common.gypi'
  ],
  'targets': [
    {
      'target_name': 'hellogyp',
      'type': 'static_library',
      'sources': [
        'hello.cc',
      ],
      'include_dirs': [
        '..',
      ],
    },
  ]
}
