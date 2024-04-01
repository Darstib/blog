#include <stdio.h>
// 封装 强调「数据」与「操纵数据的函数」的绑定以及必要的访问控制，从而抽象出「类」和「对象」的概念
struct User
{
private: // 限制访问
    static int id, age;
    char *password;

public: // 公开不限制
    bool checkPassword(char *pw);
};

class user
{ // class与struct最大的不同在于class成员默认为为private,而struct默认public
public:
    static int id, age;
};

// typedef struct User Users;
// typedef struct user users;

int main()
{
    user a;
    // printf("%d", User::id);//error:编译错误 'int User::id' is private within this context
    printf("%d", a.id); // error:编译错误 'int User::id' is private within this context
}