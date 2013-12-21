//
//  HGAppDelegate.m
//  hellogyp
//
//  Created by Olli Wang on 12/21/13.
//  Copyright (c) 2013 Olli Wang. All rights reserved.
//

#import "HGAppDelegate.h"

#import "HGRootViewController.h"

@implementation HGAppDelegate

- (BOOL)application:(UIApplication *)application
      didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
    self.window = [[UIWindow alloc]
        initWithFrame:[[UIScreen mainScreen] bounds]];
    // Override point for customization after application launch.
    self.window.backgroundColor = [UIColor whiteColor];
    self.window.rootViewController = [HGRootViewController new];
    [self.window makeKeyAndVisible];
    return YES;
}

@end
