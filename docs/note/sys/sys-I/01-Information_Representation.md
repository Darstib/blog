---
tags:
  - notes
  - sysI
comments: true
dg-publish: true
---

> [!NOTE]
>
> The number represented by the computer's internal code is called _machine number_, and the corresponding value is called _true value_.

## I Numeric

### I.1 Integer number (fixed-point)

- 关注数据储存形式
    - big endian
    - little endian

##### I.1.1.1 Unsigned integer

Just like what binary number do

$0 \leq X \leq 2^{n}-1$

##### I.1.1.2 Signed integer

###### I.1.1.2.1 Original Code

The original code representation of a number consists of the sign bit followed by the value bit, also known as sign-and-magnitude representation.

![|500](attachments/01-Information-Representation.png)

但是这样具有不少 **缺点**：

- There are two ways to represent 0!（不合直觉）
- Less range （表示的数少了一个）
- Hardware Complexity（硬件处理十分困难，如加法、乘法）

###### I.1.1.2.2 Inverse Code

> 反码能够解决一部分问题。

一个很好的解决办法是用补码表示，然后惊奇地发现所有问题都解决了，这也是补码存在的意义，在上一篇 [Inverse code & Complement code（反码&补码）](README.md#Inverse-code-&-Complement-code（反码&补码）) 的讲解也很清楚了

###### I.1.1.2.3 Complement Code

- Only one way to represent 0 
- Simple and correct addition 
- Implement subtraction with addition
- Remain the same after [sign extension](01-Information_Representation.md#sign-extension)

> 最后一条是我从后面挪过来的，也就是说在符号扩展后，表示数值不变。
>
> 例如，4 位下的 -3 的补码是 `1101`，符号扩展至 8 位后为 `1111 1101`，依旧是 -3，这也是因为 1 在取反后全部变为了 0，并不会有所影响。

![](attachments/01-Information-Representation-28.png)

对于一个 N 位二进制数来说，$M = 2^N$ 。

![|500](attachments/01-Information-Representation-2.png)

> [!QUESTION]
>
> 如果是 $[X_{T}]c \to [-X_{T}]c$ 呢？
> 
> 连带着符号位一起取反就好了。

#### I.1.2 number range

![|500](attachments/01-Information-Representation-3.png)

![|500](attachments/01-Information-Representation-4.png)

#### I.1.3 Floating-point number representation

#### I.1.4 sign change

我们在使用过程中不免碰到无符号整型和有符号整型相互转换，虽然我们可能能够实现，但是往往会存在许多安全漏洞

> [!note]
>
> 在 C 语言中我们有显式转换和隐式转换。
>
> 其中，显式转换如下：
> 
> - tx = (int) ux;
> 
> - ux = (unsigned) tx;
>
> 而对于隐式转换常出现在比较运算中，如 `>= == !=` 中，下面是一些例子，但是都遵循以下特点：
>
>> [!attention]
>>
>> If there is a mix of unsigned and signed in single expression, signed values implicitly cast to unsigned
>
> ![](attachments/01-数字系统与信息-3.png)
> [!NOTE]
>
>  "显式转换的危害"
>  

  显式转换也是强制转换，这意味着如果不怀好意就可以干一些坏事，看下面一个例子

```c++
  #include <iostream>
  using namespace std;
  int main()
  {
    cout << (((unsigned)-5) > 12) << endl;
    cout << (unsigned)-5 << endl;
  }
```

> 结果输出为 1  4294967291

##### I.1.4.1 sign extension

![|500](attachments/01-数字系统与信息-4.png)

上面是对于有符号数(t) 而言的，对于无符号数 (u) 则 **直接补 0**

###### I.1.4.1.1 example

![](attachments/01-Information-Representation-5.png)

###### I.1.4.1.2 code

```c++
#include <iostream>
#include <cstdio>
using namespace std;
int main()
{
    short int x = -15213;
    cout << x << endl;
    cout << (int)x << endl;
    printf("%u\n", x); // 将x转为无符号整型输出
    printf("%x\n", x); // 将x转为十六进制整型输出
    return 0;
}
```

-15213

4294952083

ffffc493

-15213

#### I.1.5 addition

##### I.1.5.1 unsigned addition

###### I.1.5.1.1 Truncating（数据截断）

> [!DEFINITION ]
>
> 数据截断是直接将高位丢弃，其实相当于进行了模除操作

运用在机器加法上就表现在丢弃高位的进位

![|500](attachments/01-Information-Representation-6.png)

将其可视化：

![|500](attachments/01-Information-Representation-7.png)

###### I.1.5.1.2 Mathematical Properties

Modular Addition Forms an  [Abelian Group](../../../course_notes/CS70%20DMPT/notes/18-Misc.md#^11f963):

![|500](attachments/01-Information-Representation-8.png)

##### I.1.5.2 two's complement addition

仍旧存在高位截断的情况,并且在两个较小的负数(negover) 或者两个较大正数(posover) 相加时都会产生溢出

![|500](attachments/01-Information-Representation-9.png)

因此可视化如下：

![|500](attachments/01-Information-Representation-10.png)

###### I.1.5.2.1 Mathematical Properties

![|500](attachments/01-Information-Representation-11.png)

#### I.1.6 multiplication

![|500](attachments/01-Information-Representation-12.png)

##### I.1.6.1 example

![|500](attachments/01-Information-Representation-13.png)

一个简单的例子，我们知道 int 可代表的最大数为 $2^{31}-1$ ，我们让 ele_cnt \* ele_size 等于 $2^{32}$ ，由于高位截断，实际分配的空间肯定没有这么多，但是我们确确实实拷贝了这么长的数据，会发生什么？多拷贝的数据依旧是线性排列，挤入它本不该去的地方；这十分危险。

##### I.1.6.2 implement

我们可以用 [shift operation （移位操作）](README.md#shift-operation-（移位操作）) 来实现乘法

- u << k gives $u * 2^{k}$
    - 注意高位依旧会截断
- u >> k gives $\lfloor \frac{u}{2^{k}} \rfloor$
    - 相当于移位产生了小数点然后舍去了
    - 由于数据以补码存在，即使是负数，舍去小数点依旧是向下取整

> Most machines shift and add faster than multiply, so compiler generates this code automatically
> [!QUESTION]
>
> 如果我们希望更加符合直觉，取整向 0 靠齐，即正数向下取整，负数向上取整，我们可以计算
> 
> $$\left\lfloor  \frac{x+2^{k}-1}{k}  \right\rfloor $$
> 
> 验证略

#### I.1.7 Properties of Unsigned & Two’s Comp.Arithmetic

![|500](attachments/01-Information-Representation-14.png)

> 环的概念和阿贝尔群放在一起了

![|500](attachments/01-Information-Representation-15.png)

### I.2 Float point number

> [!CITE]
>
> _IEEE Standard 754_
>
> - Nice standards for rounding, overflow, underflow
> 
> - Hard to make fast in hardware

#### I.2.1 Floating Point Representation

##### I.2.1.1 form

![|500](attachments/01-Information-Representation-16.png)

> [!INFO]
>
>  ![|500](attachments/01-Information-Representation-17.png)

其中 E 也称为 **阶码**，我们下面以单精度浮点数为例进行讲解

![|500](attachments/01-Information-Representation-22.png)

###### I.2.1.1.1 Normalized Values

这一储存形式称为 _Normalized Values_（规范化形式）

![|500](attachments/01-Information-Representation-19.png)

在我们右移操作时，对于数据溢出，在整型数中被舍去；而在浮点数中，我们用一段内存(frac) 来将其存储，即为 M（M 范围为 $[1.0,2.0)$ ，类比科学计数法不难理解），下面是一个例子

![|500](attachments/01-Information-Representation-18.png)

###### I.2.1.1.2 Denormalized Values

而当我们需要储存一个非常接近于 0 的数（exp = 000...00）时，我们不使用 normalized values，而使用 _Denormalized Values_ （非规范化形式）

- frac = 000...00 时，显然就是 0（注意+0 和-0）
- 当 frac 不为 0 时，如下：

![|500](attachments/01-Information-Representation-20.png)

###### I.2.1.1.3 Special values

当我们去储存一个很大的数时（exp = 111...11），我们使用 special values

- frac = 000..00 时，用于表示无穷
    - Represents value $\infty$ (infinity)
    -  Operation that overflows
    -  Both positive and negative
    -  E.g., 1.0/0.0 = −1.0/−0.0 = $+\infty$, 1.0/−0.0 = $-\infty$

```c++
    float x = 1.0;
    double y = 1.0;
    cout << (x / 0.0) << endl;
    cout << (y / 0.0) << endl;
    cout << (1.0 / 0.0) << endl;
    cout << (0xff / 0.0) << endl;
// 输出全为 `inf`
```

- frac 不为 0 时，则表示这不是一个数（not a number, a.k.a. NaN, Represents case when no numeric value can be determined）

E.g., sqrt(–1), $\infty - \infty ; \infty * 0$

> [!ABSTRACT]
>
> ![](attachments/01-Information-Representation-21.png)
>
> 有点绕，看看 [xg的笔记](https://note.tonycrane.cc/cs/system/cs1/topic1/#:~:text=x-%3E-k-,%E6%B5%AE%E7%82%B9%E6%95%B0%E8%A1%A8%E7%A4%BA%E6%B3%95)，详细计算的方法写的很详细，不解释了，老师也讲了（虽然看了半天才明白……）

###### I.2.1.1.4 example

![](attachments/01-Information-Representation-23.png)

![](attachments/01-Information-Representation-24.png)

> [!QUESTION]
>
>  how to compare integer with float point?
>
> ![](attachments/01-Information-Representation-25.png)
> [!NOTE]
>
> _舍入（rounding_）有四种：向偶舍入（round-to-even，默认项）、向 0 舍入（round-toward-zero）、向下舍入（round-down）、向上舍入（round-up）

###### I.2.1.1.5 Mathematical Properties of FP Mult

![|500](attachments/01-Information-Representation-26.png)

## II non-numeric

### II.1 Representation of logical values

#### II.1.1 ASCII 码

全称 _American Standard Code for Information Interchange_ ，表如下

![|500](attachments/01-数字系统与信息-5.png)

下面这段话介绍了这张表格的构成

> [!quote]
> 
> The seven bits of the code are designated by B 1 through B 7, with B 7 being the most signficant bit. Note that the most signiicant three bits of the code determine the column of the table and the least significant four bits the row of the table.

对于控制字符我们暂且不考虑。

#### II.1.2 校检位

基于 ASCII 码的七位，我们根据其中 1&0 的数量加入一个 1 / 0 (parity 1)补充成八位后发送，在接收端会同样生成校检位(parity 2)。倘若发送过程中有奇数位发生了变化，$parity_{1}\neq parity_{2}$ ，那么就发现了错误（偶数位变化另谈）

#### II.1.3 Gray code（格雷码）

专注于转轴的编码，大大节省了在相邻数字之间切换的开销

> 此处略讲，部分可以参看 [HobbitQia的笔记本](https://note.hobbitqia.cc/Logic/logic01/#gray-codes)进行学习

### II.2 Representation of Chinese Characters

![|500](attachments/01-Information-Representation-27.png)

