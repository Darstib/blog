#include <stdio.h>

struct Foo
{
    Foo()
    {
        printf("this is a ctor ¹¹Ôìº¯Êý");
    }

    // Foo() = default;
    // Foo() = delete;
};

int main()
{
    Foo f;
}