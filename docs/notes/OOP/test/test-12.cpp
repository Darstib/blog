#include <iostream>
using namespace std;

int main()
{
    int x = 2;
    int k = 3;
    int &y = x;
    cout << &x << '\n'
         << &y << endl;
    int &z = x;
    cout << &z << endl; // ͬһ��������ж������

    // &y = k;// error:lvalue required as left operand of assignment
    // ����˵���ʽ��������Ӧ���ǿ��޸ĵ�
}