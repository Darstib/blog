#include <iostream>
using namespace std;

class Count
{
    int s = 0;

public:
    ~Count(); // 析构函数，定义在第16行

    Count(int s) { this->s = s; } // 构造函数
    int getS() { return s; }
    void sPlus() { s++; }
};

Count::~Count() { cout << this->s << " "; } // 输出s

// 调用构造函数
Count count5(555);
static Count count6(666);
Count count7(777);

void f() { static Count count9(999); }

int main()
{
    Count *count1 = new Count(111);
    Count *count2 = new Count(222);

    Count count3(333);
    Count count4(444);

    f(); // 静态声明，不妨把f()相当于内联替换一样放过来

    static Count count8(888);

    delete (count1);

    for (int i = 1; i <= 5; i++)
        for (Count c(1); c.getS() <= i; c.sPlus())
            ; // 这些函数都只有一句话，不含参，不如替换过来，为了出题写的繁复罢了
    return 0;
}

/* 考察析构函数的调用，就是在考察构造函数的生命周期

基于源代码中的注释，我们直接从main函数出发
开头一大堆声明定义先不管，因为他们都没用完，不调用析构函数

37行：释放count1, 触发析构函数，输出 111
39：进入循环，i = 1
40：构造函数，命名为c，传参即s为1，结束循环时s为2，c函数使用完毕，释放，输出2（由循环知依次输出3 4 5 6 ）

循环结束，main函数也就结束了，但此时全局和静态声明的还不用释放，又析构与构造顺序相反，故输出444 333
（222不输出，因为这是我们自己取的空间，只能手动释放或者在析构函数里面帮我们释放）
剩下的同样顺序相反，888 999 777 666 555

 */
