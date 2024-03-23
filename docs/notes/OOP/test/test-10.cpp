#include <iostream>
using namespace std;

struct foo
{
    void operator=(foo)
    {
        cout << "foo called" << endl;
    }
};
class bar
{
    foo a, b, c;
};
int main()
{
    bar x, y;
    x = y; /* 相当于x.operator=(y)，那么将对y中的abc分别做编译器自动生成的拷贝赋值
     x::a.operator=(y::a.operator);……一共三次*/
}