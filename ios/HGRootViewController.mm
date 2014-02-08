// Copyright 2014 Ollix
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#import "HGRootViewController.h"

#include "hellogyp/hello.h"

@implementation HGRootViewController

- (id)init {
  if((self = [super init])) {
    _hello = new hellogyp::Hello();
  }
  return self;
}

- (void)dealloc {
  delete _hello;
}

- (void)loadView {
  [super loadView];

  _label = [[UILabel alloc] initWithFrame:self.view.frame];
  _label.text = [NSString
      stringWithUTF8String:_hello->GetGreetingMessage().c_str()];
  _label.textAlignment = NSTextAlignmentCenter;
  [self.view addSubview:_label];
}

@end
