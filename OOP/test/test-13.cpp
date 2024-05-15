#include <iostream>
using namespace std;

class Matrix
{
    int date[100][100];

public:
    Matrix operator+(Matrix &mat) // 如果这里漏了&,相当于把实例拷贝复制，那么就会经过析构
    {
        cout << "fun1" << endl;
        return *this;
    }
    Matrix()
    {
        cout << "ctor called" << endl;
    }
    ~Matrix()
    {
        cout << "dtor called" << endl;
    }
};

void f(Matrix &m1, Matrix &m2)
{
    cout << "f begin" << endl;
    const Matrix &M1 = m1 + m2;
    Matrix M2 = m1 + m2;
    m1 + m2; // 注意，在M1,M2地址输出前就触发了析构函数且只有一次，析构的正是29行
    // cout << &(m1 + m2) << endl; // error: taking address of rvalue [-fpermissive] 不要去取临时对象的地址
    cout << &M1 << '\n'
         << &M2 << endl;
    cout << "f end" << endl;
}
int main()
{
    Matrix m1, m2; // ctor called x2
    f(m1, m2);
    return 0; // dtor called x4, 具体析构顺序可以根据之前所讲类推
}