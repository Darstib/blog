struct A
{
    A() {}         // converting constructor (since C++11)
    A(int) {}      // converting constructor
    A(int, int) {} // converting constructor (since C++11)
};

struct B
{
    explicit B() {}
    explicit B(int) {}
    explicit B(int, int) {}
};

int main()
{
    A a1 = 1;      // OK: copy-initialization selects A::A(int)
    A a2(2);       // OK: direct-initialization selects A::A(int)
    A a3{4, 5};    // OK: direct-list-initialization selects A::A(int, int)
    A a4 = {4, 5}; // OK: copy-list-initialization selects A::A(int, int)
    A a5 = (A)1;   // OK: explicit cast performs static_cast, direct-initialization

    //  B b1 = 1;      // error: copy-initialization does not consider B::B(int)
    B b2(2);     // OK: direct-initialization selects B::B(int)
    B b3{4, 5};  // OK: direct-list-initialization selects B::B(int, int)
                 //  B b4 = {4, 5}; // error: copy-list-initialization selected an explicit constructor
                 //        B::B(int, int)
    B b5 = (B)1; // OK: explicit cast performs static_cast, direct-initialization
    B b6;        // OK, default-initialization
    B b7{};      // OK, direct-list-initialization
    //  B b8 = {};     // error: copy-list-initialization selected an explicit constructor
    //        B::B()
}