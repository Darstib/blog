#include <stdio.h>

class Foo // error: 'Foo::Foo()' is private within this context
{
    Foo()
    {
        printf("this is a ctor ���캯��");
    }
};
int main()
{
    // Foo f;
}