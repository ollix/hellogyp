# Copyright 2014 Ollix
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
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
