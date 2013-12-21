//
//  HGRootViewController.mm
//  hellogyp
//
//  Created by Olli Wang on 2013-12-21.
//  Copyright 2013 Olli Wang. All rights reserved.
//

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
