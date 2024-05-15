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
// void f(const int) // redefinition of 'void f(int)'  也就是说 int 和 const int 做参数是一样的
// {
//     cout << 3 << endl;
// }
void f(const int &)
{
    cout << 4 << endl;
}
int main() // 如果不注释语句，一个都跑不通，而这样vscode就不报错了
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