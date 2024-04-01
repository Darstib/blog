#include <cstdio>

void h(int &r) { puts("int &"); }
void h(const int &r) { puts("const int &"); }

int main()
{
    int x = 1;       // Overload #1
    const int y = 2; // Overload #2

    h(1); // OK, only #2 valid
    h(x); // OK, #1 called as x -> 'int&' is better than x -> 'const int&'
    h(y); // OK, only #2 valid
}