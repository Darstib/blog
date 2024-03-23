#include <iostream>
#include <string>

using namespace std;

class Complex
{
    double r, i;

public:
    Complex(double r) : r(r), i(0){};
    Complex(double r, double i) : r(r), i(i){};
    operator string() const
    {
        cout << "operator string" << endl;
        return to_string(r) + " + " + to_string(i) + 'i';
    }
    explicit operator double() const
    {
        cout << "operator double" << endl;
        return r;
    }
    explicit operator bool() const
    {
        cout << "operator bool" << endl;
        return r != 0 || i != 0;
    }
};

void foo(double x) {}

int main()
{
    Complex c = 3;  // implicit conversion, calls Complex(3)
    string str = c; // implicit conversion, calls Complex::string()

    foo(double(c)); // OK, explicit conversion
    foo((double)c); // OK, explicit conversion
    // foo(c);          // Error: no matching call to 'foo', because no implicit conversion from Complex to double

    // bool b = c;      // Error: no implicit conversion from Complex to bool
    if (c)
    { // OK, this context considers explicit operator bool
        cout << str;
    }
    return 0;
}