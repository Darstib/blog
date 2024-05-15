#include <cstdio>

struct C
{
    // 下面利用了重载解析，为了区分我们将在每一个"C"后面加上`1`2`以示区别
    C(int) // 1
    {
        puts("ctor1 called");
    } // #1: non-delegating constructor

    C()         // 2
        : C(42) // 1
    {
        puts("ctor2 called");
    } // #2: delegates to #1
    // C(char c) : C(42.0) {}  // #3: ill-formed due to recursion with #4
    // C(double d) : C('a') {} // #4: ill-formed due to recursion with #3
};

int main()
{
    // C C; 这里原文很坏地用了两个C，这不是让本就混乱的头脑更乱了嘛
    C         // 1
        name; // 其实后面的'C'只是一个名字罢了，前面的才是我们的C//1
}