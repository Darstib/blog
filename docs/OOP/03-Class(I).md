# Class(I)

同样是转移的时候没注意，全部乱码了，也不知道怎么去解决，先放着不管了
（不知道这是什么格式的编码导出的 QWQ）

[TOC]

## I �����Ͷ��������

- ����������������������뵽������
- ������������һ�֣�ָ������Щ��������ֶ�Ӧ��ʵ�����Ա�ʹ�õ�����

���ǿ�����Ϊ��������һ�������������������standard��ô˵

> [basic.pre#5]: Every name is introduced by a declaration
> [basic.def#2]: Each entity declared by a declaration is also defined by that declaration unless:
    it declares a function without specifying the function's body
    it contains the extern specifier or a linkage-specification (extern "C" {}) and neither an initializer nor a function-body,
    ...

���������롹�����ǿ����ظ��Ҷ�ε�

- extern int i;
- extern int i;
- int f(int);
- int f(int x);

����������ǺϷ��ġ�����ֻ�� i �� f ���������Ƕ��塣

�������䶼�Ƕ��壺

- int a;                          // defines a
- extern const int c = 1;         // defines c
- int f(int x) { return x+a; }    // defines f and defines x
- struct S { int a; int b; };     // defines S, S?::?a, and S::b
- enum { up, down };              // defines up and down
- S anS;                          // defines anS

## II member

���ͱ���������Ҳ��������ĳ�Ա���������������������ͬ���� access-specifier ��Ӱ�졣���磺

    struct Foo {
        using elem = int;
        elem x;     // OK, x has type int
        elem add(elem v) { x += v; return x; }
    private:
        using type = char;
        type c;     // OK, c has type char
    };

    // elem y;      // Error: unknown type name 
    ÿ����Ա�������ᱻ��Ϊ��һ�� implicit object parameter�������� calling object��

���ڳ�Ա�����ĺ������У�this ����ʽ��ֵ���� implicit object parameter �ĵ�ַ��
��Ա�����ĺ������У������κγ�Աʱ���ᱻ�Զ����� this->

����`void Foo::bar(int v) { x += v; }`���е�`x += v;`ʵ���� `this->x += v;`��

## III inline substitution

�ȿ�����Ĵ���

    struct User {
    private:
        int id, age;
        char* password;
    public:
        bool checkPassword(char* pw); // check if pw == password
        void setAge(int v) {
            if (v >= 0)
                age = v;
        }
        int getAge() { return age; }
        // ...
    };

### III.1 inline substitution

��C++�У����ú�����ζ��Ч�ʽ��ͣ�������������ϣ���ġ���ˣ�ͨ������**inline substitution�������滻��**�������������滻�뱻���ô������⺯������ת����������һ���̶����Ч�ʣ��Ƚ������ں��滻��
��ô��ʲô���ĺ����ᱻ�����أ�

- �� C with Classes �У�ֻ����Щ������д����Ķ��еĳ�Ա�����ſ��ܻᱻ��������vscode���Ұ����ŵ����еĺ����Ͽ��Կ���
- �ں�����C++�У�inline�ؼ��ֱ����룻�����ں��������У�����
`inline int foo(int x) { return add5(x); }`

�����������һ��**����**������Ӧ�����ȿ���ʹ�������滻����ͨ���ĺ�������~~����ͨ���ᱻ����~~�����������Զ��ж��Ƿ�Ӧ�ü���inline�ؼ��֣���Ӧ���Ǳ����Ǹ������Ƿ�Ӧ�ü��ϵģ����Բ�Ҫ�����������

### III.2 ȱ��

�������� ÿ�� ���ñ�չ�����������������ĺ����ǳ�����ᵼ�����ɵ�Ŀ�����ܴ�������**�ڴ���Ż��߾ֲ�������**����Ҳ���ܻ�����ܲ���һ��Ӱ�졣

���������� C ������ function-like macros ��һ���õ��滻��

> �����������Ա�������������Ҫ�Ķ�������������ע�������ͨ��������ڿ��ֶΡ�

## IV constructor

**���캯��**(constructor)��һ������ĳ�Ա���������ڳ�ʼ������Ķ���,Ҳʱ������дΪ`ctor`��`c'tor`�ȡ�

### IV.1 ����

ʹ����Ա�ܹ�������ĳ��**��֤**��������Ա�����������������֤

    class Container {
        elem* val;
        // ...
    public:
        Container() {
            val = nullptr;
        }
        // ...
    };

**��֤**���� val ��ֵҪô�� nullptr����ָ�룬��NULL��������Եȿ���function overloading��[`test-06.cpp`](test/test-06.cpp)����Ҫô��������Ա��������ֵ���������Ǹ������ֵ

�������Ϳ���ʹ�� Container c = Container();����һ����������������󡣲��Ͻ���˵���������佫���� c �󶨵��˶�Ӧ�����������ϡ�
Ϊ�˴�����Ӽ����գ�C++ �������Ӽ���д����Container c;[`test-01.cpp`](test/test-01.cpp)
���ڶ���һ������ʱ��Ҫ�õ����캯����������Ҫ�õĹ��캯���� private �ģ�������޷������죺[`test-02.cpp`](test/test-02.cpp)

���캯�������û�**����һ����ʼ��С**��Ȼ��ֱ�ӿ�һ����Ӧ��С�Ŀռ䣺

    class Container {
        elem* val;
        // ...
    public:
        Container(unsigned size) {
            val = (elem*)malloc(sizeof(elem) * size);
            // ...
        }
        // ...
    };

����ʹ�� Container c2 = Container(64); ����һ���Զ����С������
ͬ���أ�C++ �������Ӽ���д����Container c2(64);

��Ȼ���޲ι���ʱ��Ҫ�����ţ����������ж�Ϊ��ͨ����

> �� C++ �У���������ʱ�� ��ʼ���� (initializer) �������� int a = 4; �� = -clause ֮�⣬�������� int a(4); �� ( expression-list )��

### IV.2 new & delete

���ǣ�ͨ��`malloc`��ȥ����ռ䣬��������ǲ��ᱻִ�еģ�C++������һ���µĹؼ��ֽ�`new`����ɷ����ִ��˫����
new ����ʽ����������������������飺
- int * p1 = new int;
- int * pa = new int[n];[`test-03.cpp`](test/test-03.cpp)

���ڿռ��ͷţ�free����������ԣ�C++������`delete`�ؼ���
- ��� p �� new ��ʱ�򴴽����ǵ���������Ӧ���� delete p; ����ʽ (single-object delete expression) ����
- ��� p �� new ��ʱ�򴴽��������飬��Ӧ���� `delete[] p;` (array delete expression) ����ʽ����
- ������ δ������Ϊ (**UB, undefined behavior**)������һ�ֺ�Σ�յ���Ϊ��Ӧ������

### IV.3 default arguments

C++�ں���������֧��**Ĭ�ϲ���(default arguments)**,������������������ʡ��<ins>ĩβ</ins>�����ɲ����ķ�ʽ���ã�

    void point(int x = 3, int y = 4);
    //��δ���¸������ʱʹ��Ĭ�ϲ���
    point(1, 2); // calls point(1, 2)
    point(1);    // calls point(1, 4)
    point();     // calls point(3, 4)

    ʡ��ĩβ�ܺ�����ģ��Ͼ��������������

    > void point(int x = 1, int y);
    > point(2);

    �����Ǹ��ǵ�һ�����ǽ��������ڶ���������������� 

������һ�ص㣬���ǿ��Խ����õĲ�����ΪĬ�ϲ����������Ч��

### IV.4 function overloading

���һ���������ö�����������ǵĲ�����ͬ�������Ϊ**��������(fuction overloading)**
��ʹ�������ĺ�����ʱ�򣬱��������������Ǵ���Ĳ�������������ʹ���ĸ���������̳�Ϊ**���ؽ���(overload resolution)**

> ���ؽ����Ĺ����ǱȽϸ��ӵģ�һ������ô������
> 1. ƥ�亯�������γ�**��ѡ������**(candidate)
> 1. �������б��γ�**���к�����**
> 1. ͨ��һ������Ƚ���Щ������ֻ���ܹ�ѡ��**һ��������ƥ��**�ĺ������ܼ������У�����������

ע�⵽�����������ؽ���ʱ�Ƚϵ���**��������**��**�����б�**����ʱ��Ҫȥ��`Ĭ�ϲ���`��������������з���ֵ��ͬ�ĺ����ǲ��ܹ����صġ�[`test-04.cpp`](test/test-04.cpp)

��ô��ǿ����Ҫ��:��Ҫ����`Ĭ�ϲ���`��ô�죿~~����~~
ϣ�������ܹ�ͨ��[`test-05.cpp`](test/test-05.cpp)����

### IV.5 ˼����

> **˼��**�������ڽ����캯��֮ǰ�Ĵ����ﶼû��д���캯������������Ҳ�������������У�C++ Ҳϣ����û�б�Ҫ������ʱ���� C ���������ݣ��� C �е� struct Ҳû��д���캯������������Ҳ�ܱ����С�������ô�����أ�
> **���**����ʵ�ϣ�����һ���࣬����û�û���ṩ�κι��캯��������������Զ�Ϊ����ഴ��һ�� public �� **implicitly-declared default constructor**����������Ϊ defaulted��Defaulted �Ĺ��캯���������κβ�����Ҳʲô��������������κ��û��ṩ�Ĺ��캯������ defaulted default constructor ������Ϊ deleted �ġ�deleted �ĺ������ܱ����á�
����������û��ṩ�˹��캯��������Ȼ������ ClassName() = default; ������ defaulted �Ĺ��캯����
�û�������ͨ�� ClassName() = delete; ��ʽ�ؽ� default constructor ���ó� deleted �ġ�

### IV.6 member initializer lists

�����Ǵ���һ���û�ʱ��

    class User {
        int id, age, failTimes;
        char* password;
    public:
        User(int id, int age, char* pw) {
            this->id = id;
            this->age = age;
            failTimes = 0;
            password = copyStr(pw); // assume that `copyStr` gets a string     // and allocate some space and copy it
        }
        // ...
    };

����ÿ������д�����е��鷳�����������**member initializer lists**�����£�

    class User {
        int id, age, failTimes;
        char* password;
    public:
        User(int id, int age, char* pw) : id(id), age(age), failTimes(0), password(copyStr(pw)) {}
        // ...
    };

��Щ��ʼ�����ڹ��캯���ĺ�����ִ��֮ǰ����

> �����÷���ʵƽʱҲ�����ã�����`int a(4);`���Ƕ�����һ�����ͱ���a����ֵΪ4

��һЩ����£�member initializer lists �Ǳ�Ҫ�ġ����磺

    class Point {
        int x, y;
    public:
        Point(int x, int y) : x(x), y(y) {}
    };

    class Circle {
        Point c;
        int r;
    public:
        Circle(int cx, int cy, int r) : c(cx, cy), r(r) {}
    };
���е����ڶ��е�c(cx, cy)�Ǳ����
> C++ �涨���ڹ��캯���ĺ�����ִ��֮ǰ�����в���
> - Ҫô��Ĭ�Ϸ�ʽ��ʼ��
> - Ҫô���� member initializer lists ��������ʼ��
> 
��������Ķ��󣬡�Ĭ�Ϸ�ʽ��ʼ������ζ��ʹ�� default constructor ����
Ȼ����Point �ಢû�� default constructor(x, y��û�и���ֵ)
������ member initializer lists û��ָ�� Point ��ĳ�ʼ����ʽ���ͻ���ֱ������`error:no matching function for call to 'Point:Point()'`

> ע�⣺
> - ������캯�������붨��ֿ���initializer lists Ӧ�ó����ڶ����� 
> - ���캯����Ա��ʼ��˳�����ɰ��ն���˳�����initializer lists �е�˳��һ����˵���߶�һһ��Ӧ�ǿ϶����ٺò����ˣ�

#### IV.6.1 delegating constructor

member initializer list ���Խ�����ί�и�ͬһ���͵���һ�����캯����������һί�еĹ��캯����Ϊ **delegating constructor��**
��������Ļ���member initializer list Ӧ��<u>ֻ������һ����Ŀ</u>��
Ŀ�깹�캯�������ؽ���ѡȡ�������н�����delegating constructor �ĺ����屻ִ��
һ�����캯������ֱ�ӻ��ӵر�ί�и��Լ�����Ϊ�������������һ������ѭ����������������test-07.cpp�е�#3#4����һ�����ӣ�
[`test-7.cpp`](test/test-07.cpp)

#### IV.6.2 default member initializer

**default member initializer** �������Ǹ�һ�����飬���£�

    class User {
        int id, age = -1, failTimes = 0;
        char* password = nullptr;
    public:
        User(int id, int age, char* pw) : id(id), age(age), password(copyStr(pw)) {}
        User(int id, int age) : id(id), age(age) {}
        User(int id) : id(id) {}
        // ...
    };

�����ڸ������Ա��ͬʱ���˳�ֵ����ʹ�����������Щ������Ҫ����ʹ��ʱ�������ܹ���������ΪĬ��ֵ(default)������������Ҫһ����֮ͬ��ʱ�������ֿ��԰�����ǰ������ȥ��ֵ��Ҳ����˵��**��ǿ���˲�ͬ�Ҿ͸ģ���˵����������**�����������Ҳ�Ǻܷ������ǵ�ϰ�ߵģ�֮�����ǲ���ǿ��

> �ڸ�ֵʱ���뾡��ʹ��`=`����ΪһЩ���ʵ�ڳ�������
> ����`User user(����)`������ʵ�е����� ~~��Ȼ����Ҳȷʵ�ǹ��캯���������ֿ�������ͨ��������~~

## V destructors

ÿ��ʹ��`malloc`��ʱ��Ҫ�����ֶ�`free`�ͷ��ڴ棬������������ã�̫�鷳��
C++ ������**��������(destructors)**������������������һ����������ÿ��������������ڽ�����ʱ�򱻵��ã����������������ͷŶ��������й����п��ܻ�ȡ����Դ�������ͷ�������ڴ桢�رմ򿪵��ļ��ȣ������������Լ�ȥ�ж�ʲôʱ���ȥ����Щ���飩

������������ `~className()`������ ~ Ҳ������ȡ�����������������ʾ���빹���෴���ĺ��壬������

    class Container {
        elem* val;
        // ...
    public:
        Container(unsigned size) {
            val = (elem*)malloc(sizeof(elem) * size);
            // ...
        }
        ~Container() { // ��������
            free(val); // ��valָ����ڴ��ͷ�
        }
    };

���������Ĳ����б���Զ�ǿյģ���ˣ������������޷����صģ�

�빹�캯�����Ƶģ�����Ҳ��implicitly-declared destructor������������ǰ��[˼����](#˼����)���һ�������ǲ��ٽ���

��� Foo ������������ deleted �ģ����ߵ�ǰ�����⣬��������������private�ģ������ڵ�ǰλ�ò��ɷ��ʣ�����ô����`Foo f;`��ȫ�ֱ������ֲ��������߳�Ա���������ǷǷ��ġ���Ϊ��������Ϊ���޷�����������������ô��������˹��캯���޷��ͷţ�Ҳ�Ͳ����㶨����
���ǣ���������£�����ͨ�� new ������һ����̬�Ķ�����Ϊ���������Ķ��󲢲���ʽ����ͬһ���������ڵ�������������ǰ������֪�����ǿ�����delete�����������������ǻ����ֶΣ���ȻҲ�ͷ�����

### V.1 �����������ʱ����˳��

����һ������������������� (lifetime)�����ĳ�ʼ�������죩��ɿ�ʼ�������������������ñ�����Ϊֹ
�κ�һ�����󶼻�ռ��һ���ִ洢���ⲿ�ִ洢����С�������ڳ�Ϊ�������� storage duration������� lifetime ���ڻ򱻰������� storage duration

> ����˵����С�������ڡ�������Ϊ���������󣬶�Ӧ�Ĵ洢��Ȼ���Ա����̻��գ���Ҳ��һ�����̱����ա�������С���ṩ����һ�ֱ�֤����Ҳû�㶮���ȷ��ţ�

- �� C++11 ֮ǰ���κ�һ������� storage duration ��������һ�֣�
    - automatic storage duration: û�б�����Ϊ static�ľֲ�����
    - static storage duration: non-local ���󣬻��߱�����Ϊ static �ľֲ�����������Ա����
    - dynamic storage duration: new �����Ķ���
�Ӷ��� (subobject�����Ա����) �� storage duration �������ڵĶ���� storage duration��

- �����������£�**���캯���ᱻ����**��
    - ����ȫ�ֶ����� main() ��������֮ǰ��������ͬһ�����뵥Ԫ�ڶ������һ���������ʹ��֮ǰ����ͬһ�����뵥Ԫ�ڣ����ǵĹ��캯������������˳���ʼ����
    - ���� static local variables���ڵ�һ�����е�����������ʱ��
    - ���� automatic storage duration �Ķ�����������������ʱ��
    - ���� dynamic storage duration �Ķ���������`new`����ʽ����ʱ��

- �����������£�**���������ᱻ����**��
    - ���� **static** storage duration �Ķ����ڳ������ʱ��**�����빹���෴��˳��**
    - ���� **automatic** storage duration �Ķ��������ڵ� block �˳�ʱ��**�����빹���෴��˳��**
    - ���� **dynamic** storage duration �Ķ����� delete ����ʽ�С�
    - ������ʱ���󣬵����������ڽ���ʱ�����ǻ��ں�����½�������ʱ�������������� ~~����~~��

����Ԫ�ص�������������˳�����乹��˳���෴[`test-08.cpp`](test/test-08.cpp)
���Ա������˳��Ҳ���乹��˳���෴

xuan-insrѧ��Ϊ����������һ���⣬����д�������

    class Count{
        int s = 0;
    public:
        ~Count();

        Count(int s) { this->s = s; }
        int getS(){
            return s;
        }
        void sPlus(){
            s++;
        }
    };

    Count::~Count() { cout << this->s << " ";}

    Count count5(555);
    static Count count6(666);
    Count count7(777);

    void f(){
        static Count count9(999);
    }

    int main() {
        Count *count1 = new Count(111);
        Count *count2 = new Count(222);

        Count count3(333);
        Count count4(444);

        f();

        static Count count8(888);

        delete(count1);

        for(int i = 1; i <= 5; i++)
            for(Count c(1); c.getS() <= i; c.sPlus());

        return 0;
    }

�������Կ�[`test1.cpp`](test/test1.cpp) 
���н��`111 2 3 4 5 6 444 333 888 999 777 666 555 `

�����û��������[`xyxѧ������Ƶ����`](https://www.bilibili.com/video/BV1ML411r7dV/?spm_id_from=333.788&vd_source=0a037c4dd2becee04d2b1ccafdc1862e)

## VI The End
