#include <cstdio>

int f(double){};
// void f(double){}; // Ϊ�˲��ò���������ܾ���ע����

int main()
{
    f(2.0); // error: ambiguating new declaration of 'float f(double)'
}