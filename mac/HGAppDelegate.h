//
//  HGAppDelegate.h
//  HelloGyp
//
//  Created by Olli Wang on 12/23/13.
//  Copyright (c) 2013 Ollix. All rights reserved.
//

#import <Cocoa/Cocoa.h>

@interface HGAppDelegate : NSObject <NSApplicationDelegate>

@property (weak) IBOutlet NSTextField *label;
@property (assign) IBOutlet NSWindow *window;

@end
