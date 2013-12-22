// Copyright (c) 2013 Ollix. All rights reserved.
//
// ---
// Author: olliwang@ollix.com (Olli Wang)

#ifndef HELLOGYP_HELLO_H_
#define HELLOGYP_HELLO_H_

#include <string>

namespace hellogyp {

class Hello {
 public:
  Hello();
  ~Hello();

  std::string GetGreetingMessage() const;
};

}  // namespace hellogyp

#endif  // HELLOGYP_HELLO_H_
