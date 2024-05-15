#include <stdio.h>

class Foo // error: 'Foo::Foo()' is private within this context
{
    Foo()
    {
        printf("this is a ctor ¹¹Ôìº¯Êý");
    }
};
int main()
{
    // Foo f;
}