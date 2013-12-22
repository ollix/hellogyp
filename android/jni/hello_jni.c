//
//  native.c
//  hellogyp
//
//  Created by Olli Wang on 2013-12-22.
//  Copyright 2013 Olli Wang. All rights reserved.
//

#include <jni.h>

/* This is a trivial JNI example where we use a native method
 * to return a new VM String. See the corresponding Java source
 * file located at:
 *
 *   apps/samples/hello-jni/project/src/com/example/hellojni/HelloJni.java
 */
jstring Java_com_example_hellogyp_MainActivity_stringFromJNI(JNIEnv* env,
                                                             jobject thiz ) {
  return (*env)->NewStringUTF(env, "Hello from JNI!");
}
