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
    Foo *p = new Foo(5); // �˴���Ϊ�������5
    puts("===");
    Foo *pa = new Foo[5]{1, 2, 3, 4, 5}; // ���������飬����ĳ�ʼ����Ϊ�������������{����}�ֱ�������
}