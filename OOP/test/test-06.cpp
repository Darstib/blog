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
    // f(NULL);//��������ƥ��
    f(nullptr); // ���B,˵��nullptr�������ڱ�ʾ��ָ��
    /* ʲô��������C��������ô����
    C��û��nullptr�����ء��� */
}