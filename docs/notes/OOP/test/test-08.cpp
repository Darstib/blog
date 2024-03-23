#include <cstdio>

struct A
{
    int x;
    A(int x) : x(x)
    {
        printf("B %d\n", x);
    }
    ~A()
    {
        printf("D %d\n", x);
    };
};

int main()
{
    A *p = new A[5]{1, 2, 3, 4, 5}; // []里缺少5会有提示“不允许使用不完整的类型
    delete[] p;
    return 0;
}