// Copyright (c) 2013 Ollix. All rights reserved.
//
// ---
// Author: olliwang@ollix.com (Olli Wang)

#include "hellogyp/hello.h"

namespace hellogyp {

Hello::Hello() {}

Hello::~Hello() {}

std::string Hello::GetGreetingMessage() const {
  return "Hello GYP!";
}

}  // namespace hellogyp
