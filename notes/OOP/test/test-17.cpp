#include <iostream>
using namespace std;

struct foo
{
    foo()
    {
        cout << "ctor called" << endl;
    }
};

int main()
{
    foo f1 = foo();
    foo f2 = foo::foo();
    /* error: cannot call constructor 'foo::foo' directly [-fpermissive]
       15 |     foo f2 = foo::foo();
          |              ~~~~~~~~^~
    test-17.cpp:15:22: note: for a function-style cast, remove the redundant '::foo' */
}