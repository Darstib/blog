#include <iostream>
using namespace std;

struct T
{
    T() { cout << "ctor called" << endl; }
    T(const T &)
    {
        cout << "copy ctor called\n";
    }
    ~T() { cout << "dtor called\n"; }
};
T f()
{
    return T();
}

int main()
{
    f();
    cout << "====" << endl;
    T t = f();
}