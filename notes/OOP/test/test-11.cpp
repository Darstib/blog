#include <iostream>
using namespace std;

const int M = 100;
class Matrix
{
    int data[M][M];

public:
    Matrix operator+(Matrix mat)
    {
        cout << "func 1"
             << endl;
        return *this;
    }
    Matrix operator*(int x)
    {
        cout << "func 2"
             << endl;
        return *this;
    }
    Matrix operator*(Matrix mat)
    {
        cout << "func 3"
             << endl;
        return *this;
    }
};
Matrix operator*(int x, Matrix mat)
{
    cout << "func 4"
         << endl;
    return mat;
}

int main()
{
    Matrix a, b;
    a + b; // 1
    a * 1; // 2
    1 * a; // 4
    a *b;  // 3
}