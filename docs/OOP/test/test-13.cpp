#include <iostream>
using namespace std;

class Matrix
{
    int date[100][100];

public:
    Matrix operator+(Matrix &mat) // �������©��&,�൱�ڰ�ʵ���������ƣ���ô�ͻᾭ������
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
    m1 + m2; // ע�⣬��M1,M2��ַ���ǰ�ʹ���������������ֻ��һ�Σ�����������29��
    // cout << &(m1 + m2) << endl; // error: taking address of rvalue [-fpermissive] ��Ҫȥȡ��ʱ����ĵ�ַ
    cout << &M1 << '\n'
         << &M2 << endl;
    cout << "f end" << endl;
}
int main()
{
    Matrix m1, m2; // ctor called x2
    f(m1, m2);
    return 0; // dtor called x4, ��������˳����Ը���֮ǰ��������
}