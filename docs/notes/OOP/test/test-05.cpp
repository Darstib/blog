#include <cstdio>

void f(int i = 0)
{
    printf("A");
};
void f()
{
    printf("B");
};
// ��ʱ����������û������ģ�����������þ���������
int main()
{
    f(1); /*  ���������У��������滹�ǲ��е�
    ��Ϊ��֪���ǵ����˵�һ�����ز�ʹ��Ĭ�ϲ���or���õڶ�������*/
    // f();//error: call of overloaded 'f()' is ambiguous
}