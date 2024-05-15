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
    cout << &z << endl; // 同一对象可以有多个引用

    // &y = k;// error:lvalue required as left operand of assignment
    // 即是说表达式左侧操作数应该是可修改的
}