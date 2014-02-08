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

#import "HGAppDelegate.h"

#include "hellogyp/hello.h"

@implementation HGAppDelegate

- (void)applicationDidFinishLaunching:(NSNotification *)aNotification {
  // Insert code here to initialize your application
  auto hello = hellogyp::Hello();
  NSString *greeting = [NSString
      stringWithUTF8String:hello.GetGreetingMessage().c_str()];
  [self.label setStringValue:greeting];
}

@end
