#include <cstdio>

class Foo
{
    int x;
};

class Container
{
    using elem = Foo;
    elem *val;
    unsigned size = 0, capa;
    // ...
public:
    Container(unsigned capa) : val(new elem[capa]), capa(capa) {}
    ~Container() { delete[] val; }

    void operator=(Container from)
    {
        puts("#1 called");
    }
    void operator=(elem *val)
    {
        puts("#2 called");
    }
};

int main()
{
    Container c(128);
    Foo *p1 = new Foo[100];
    Foo *p2 = new Foo;
    c = p1; // 这行输出
    c = p2; // 这行输出
    return 0;
}