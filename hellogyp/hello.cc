// Copyright (c) 2013 Ollix. All rights reserved.
//
// ---
// Author: olliwang@ollix.com (Olli Wang)

#include "hellogyp/hello.h"

namespace hellogyp {

Hello::Hello() {}

Hello::~Hello() {}

std::string Hello::GetGreetingMessage() const {
  // Uses the `auto` keyword to make sure C++11 is supported.
  auto greetings = std::string("Hello GYP!");
  return greetings;
}

}  // namespace hellogyp
