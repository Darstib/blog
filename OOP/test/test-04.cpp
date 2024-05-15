#include <cstdio>

int f(double){};
// void f(double){}; // 为了不让插件报错难受就先注释了

int main()
{
    f(2.0); // error: ambiguating new declaration of 'float f(double)'
}