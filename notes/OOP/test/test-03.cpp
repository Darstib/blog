#include <cstdio>

int a(4);
struct Foo
{
    Foo(int x)
    {
        printf("ctor %d\n", x);
    }
};
int main()
{
    printf("%d\n", a);
    Foo *p = new Foo(5); // 此处意为传入参数5
    puts("===");
    Foo *pa = new Foo[5]{1, 2, 3, 4, 5}; // 类似于数组，后面的初始化意为构造了五个对象，{数字}分别作参数
}