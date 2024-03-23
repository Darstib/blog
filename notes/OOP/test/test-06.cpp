#include <cstdio>

void f(int)
{
    printf("A");
}
void f(int *)
{
    printf("B");
}

int main()
{
    // f(NULL);//多项重载匹配
    f(nullptr); // 输出B,说明nullptr更倾向于表示空指针
    /* 什么？你问我C语言中怎么样？
    C中没有nullptr和重载…… */
}