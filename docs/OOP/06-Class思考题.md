> 补充部分建议学习完Class部分后再对细节部分巩固使用

## I Elaborated type specifiers

带有 struct 或者 class 关键字的类型名 (如 class Foo) 叫做 Elaborated type specifiersdcl.type.elab。

在 C 语言中，类似 struct x {}; int x; 是符合语法的：虽然这会使得名字 x 既表示一个结构体，又表示一个变量；但在 C 语言中这不会引起歧义，因为当 x 表示结构体时必须带上 struct 关键字；不过在 C++ 中，直接使用 x 就只能引用到变量 x 了，因为此时 int x; 的 x hides struct x {}; 的 xbasic.scope.hiding。

但是为了兼容 C，C++并没有禁止上述写法，而是规定可以通过 Elaborated type specifiers 显式地来使用结构体 x，即使用 struct xbasic.lookup.elab#1,class.name；对 class 也一样

## II name equivalence

对于类的直接赋值，要求一定是同一种类，如下：

```c++
struct x{int a;};
    struct y{int a;};
    x a1;
    y a2;
    int a3;
    a1 = a2; // error: y assigned to x
    a1 = a3; // error: int assigned to x
```
    
## III Forward Declaration

如果当前作用域没有名为 identifier 的类，那么形如 class-key attr identifier ; 的声明是一个 forward declarationclass.name

例如 class Foo;，它声明了一个叫 Foo 的类；但直到这个类被定义之前，它的类型是不完整的basic.types.general#5。

不完整的类型有一些限制，但是也有一些可以完成的操作。例如不完整的类型不能用来定义变量（包括成员变量）、作为函数声明或定义的参数或者返回值类型等；但是可以定义指向它的指针。

例如，常见的用途是，两个类可能会互相使用。这时就可以写出类似下面这样的代码：

```c++
 struct X;
    struct Y {
        X* ptr;
        // X mem; // Error: field has incomplete type 'X'
        X* foo();
    };
    struct X {
        Y* ptr;
        Y* bar();
    };
```
   
这时第 1 行是必须的，否则第 3 行的 X 就是一个未知的类型

## IV Injected Class Name

> C++ 规定，A class-name is inserted into the scope in which it is declared immediately after the class-name is seen. The class-name is also inserted into the scope of the class itself; this is known as the injected-class-name

这就是 `struct Node { Node* next; };` 能够使用 `Node` 的原因

## V function-style cast

不是！看下面的[代码](test/test-17.cpp)：

    Foo f = Foo();
    Foo f2 = Foo::Foo();

我们不能直接调用构造函数，这是因为 构造函数并没有名字，因此永远无法被用名字找到。`Foo();` 的写法并不是对构造函数的调用，而是一个 "**function-style cast**"。

> 我们知道 C 语言中的类型转换 (cast) 表达式形如 (int)3.2（称为 C-style cast），而 C++ 引入了形如 int(3.2) 的 function-style cast。int(3.2) 将 3.2 显式地转换为了一个临时的 int 对象；类似地，Foo() 也（什么都不用地）显式地转换出了一个临时的 Foo 对象。虽然这个转换本身会使用到构造函数，但是这个表达式本身不是在调用构造函数。

这个东西的重要用途之一也是模板，我们会在后面的章节中再次讨论。

## VI implicitly-declared default ctor & dtor

参见[析构函数](https://xuan-insr.github.io/cpp/cpp_restart/4_class_1/#44-%E6%9E%90%E6%9E%84%E5%87%BD%E6%95%B0)最下边