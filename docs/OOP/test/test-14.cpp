#include <iostream>
using namespace std;

// void f(int)
// {
//     cout << 1 << endl;
// }
void f(int &)
{
    cout << 2 << endl;
}
// void f(const int) // redefinition of 'void f(int)'  Ҳ����˵ int �� const int ��������һ����
// {
//     cout << 3 << endl;
// }
void f(const int &)
{
    cout << 4 << endl;
}
int main() // �����ע����䣬һ�����ܲ�ͨ��������vscode�Ͳ�������
{
    int a = 1;
    int &b = a;
    const int c = 2;
    const int &d = c;
    f(a);
    f(b);
    f(c);
    f(d);
}