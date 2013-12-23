//
//  HGAppDelegate.m
//  HelloGyp
//
//  Created by Olli Wang on 12/23/13.
//  Copyright (c) 2013 Ollix. All rights reserved.
//

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
