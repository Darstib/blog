#include <cstdio>

void f(int i = 0)
{
    printf("A");
};
void f()
{
    printf("B");
};
// 此时这样重载是没有问题的，但是下面调用就有问题了
int main()
{
    f(1); /*  这句可以运行，但是下面还是不行的
    因为不知道是调用了第一项重载并使用默认参数or调用第二项重载*/
    // f();//error: call of overloaded 'f()' is ambiguous
}