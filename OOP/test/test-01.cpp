#include <stdio.h>

struct Foo
{
    Foo()
    {
        printf("this is a ctor ���캯��");
    }

    // Foo() = default;
    // Foo() = delete;
};

int main()
{
    Foo f;
}