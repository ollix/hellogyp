//
//  hello_jni.cc
//  hellogyp
//
//  Created by Olli Wang on 2013-12-22.
//  Copyright 2013 Olli Wang. All rights reserved.
//

#include <string>

#include "hellogyp/hello.h"
#include "jni.h"

extern "C" {

jstring Java_com_example_hellogyp_MainActivity_stringFromJNI(JNIEnv* env,
                                                             jobject obj) {
  hellogyp::Hello hello = hellogyp::Hello();
  return env->NewStringUTF(hello.GetGreetingMessage().c_str());
}

}  // extern "C"
