#include <cstdio>

struct C
{
    // �������������ؽ�����Ϊ���������ǽ���ÿһ��"C"�������`1`2`��ʾ����
    C(int) // 1
    {
        puts("ctor1 called");
    } // #1: non-delegating constructor

    C()         // 2
        : C(42) // 1
    {
        puts("ctor2 called");
    } // #2: delegates to #1
    // C(char c) : C(42.0) {}  // #3: ill-formed due to recursion with #4
    // C(double d) : C('a') {} // #4: ill-formed due to recursion with #3
};

int main()
{
    // C C; ����ԭ�ĺܻ�����������C���ⲻ���ñ��ͻ��ҵ�ͷ�Ը�������
    C         // 1
        name; // ��ʵ�����'C'ֻ��һ�����ְ��ˣ�ǰ��Ĳ������ǵ�C//1
}