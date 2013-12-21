//
//  HGRootViewController.h
//  hellogyp
//
//  Created by Olli Wang on 2013-12-21.
//  Copyright 2013 Olli Wang. All rights reserved.
//

#import <UIKit/UIKit.h>

namespace hellogyp {
class Hello;
}

// This view controller displays the text returned by the GetGreetingMessage
// method of the hellogyp::Hello class.
@interface HGRootViewController : UIViewController {
 @private
  hellogyp::Hello *_hello;
  UILabel *_label;
}

@end
