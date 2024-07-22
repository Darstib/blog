## Verilog HDL

### Introduction
#### Lexical Conventions（词汇约定）

![|500](attachments/03-Combinational%20Logic%20Design.png)
![|500](attachments/03-Combinational%20Logic%20Design-1.png)

> [立即数](https://zju-sys.pages.zjusct.io/sys1/sys1-sp24/lab1-1/#_11)

![|500](attachments/03-Combinational%20Logic%20Design-2.png)

![|500](attachments/03-Combinational%20Logic%20Design-3.png)
![|500](attachments/03-Combinational%20Logic%20Design-4.png) ![|500](attachments/03-Combinational%20Logic%20Design-5.png)

#### Basic Syntax: Module, Port and Instantiate

![](attachments/03-Combinational%20Logic%20Design-6.png)

> [!ATTENTION]
>
> 当实例化的模块含参数时，参数列表应该写在 instance-identifier 前面

#### Basic Syntax: Data Type

![|500](attachments/03-Combinational%20Logic%20Design-7.png)
![|500](attachments/03-Combinational%20Logic%20Design-8.png)
### Modeling methods

#### Structured modeling

• Module-level

根据逐层调用自己构建的模块来完成复杂的工程，就像我们在 C 语言中使用函数一样

• Gate-level

通过调用门级电路来完成

• Switch-level

通过调用硬件内部的晶体管
#### Dataflow modeling

• Suitable for modeling **combinational logic circuits**

• Use continuous assignment statements: `assign`
#### Behavioral modeling

`always @(event signal list) procedure statement`
### testbench

lab 里面经常会用的，作为仿真的测试输入。
## Combinational Logic Circuit

![|500](attachments/03-Combinational%20Logic%20Design-9.png)
### 2-level vs. multi-level

|       | speed | cost |
| ----- | ----- | ---- |
| two   | fast  | high |
| multi | low   | low  |

### design

![|500](attachments/03-Combinational%20Logic%20Design-10.png)
### special value

![|500](attachments/03-Combinational%20Logic%20Design-11.png)
## Some Classic/Basic Designs

> 下面大多在 lab 中会实现
### Decoder

实验指导中的一/独热码 [one-hot code](https://zju-sys.pages.zjusct.io/sys1/sys1-sp24/lab1-2/#_4:~:text=%E6%80%A7%E6%9B%B4%E5%B7%AE%E3%80%82-,%E5%A4%8D%E5%90%88%E5%A4%9A%E8%B7%AF%E9%80%89%E6%8B%A9%E5%99%A8%E5%AE%9E%E7%8E%B0%E8%AF%91%E7%A0%81%E5%99%A8,-%E5%AF%B9%E4%BA%8E%20N%20%E4%BD%8D)，实现如下

![|500](attachments/03-Combinational%20Logic%20Design-12.png)

可以用于实现组合逻辑电路

![|500](attachments/03-Combinational%20Logic%20Design-13.png)
### Seven-Segment Display Decoder

![|500](attachments/03-Combinational%20Logic%20Design-14.png)
### Encoder

![|500](attachments/03-Combinational%20Logic%20Design-15.png)

考虑到一些不正常的输入（比如全为 0 或者多个 1），引入了 **Priority Encoder**

![|500](attachments/03-Combinational%20Logic%20Design-16.png)
### Multiplexer

![|500](attachments/03-Combinational%20Logic%20Design-17.png)
#### example

![|500](attachments/03-Combinational%20Logic%20Design-18.png)
### Demultiplexer

![|500](attachments/03-Combinational%20Logic%20Design-19.png)
### Half-Adder

![|500](attachments/03-Combinational%20Logic%20Design-20.png)

实现最基本的加法，输出结果和进位
### Full adder
#### simple full adder

![](attachments/03-Combinational%20Logic%20Design-22.png)

用两个半加器将三者加起来
#### ripple-carry adder（行波进位加法器）

![|500](attachments/03-Combinational%20Logic%20Design-21.png)

将低位的进位 Cout 输入给高位一起加，这和我们手动加法是一致的
#### carry-lookahead adder（超前进位加法器）

## Timing Analysis

![|500](attachments/03-Combinational%20Logic%20Design-23.png)

![|500](attachments/03-Combinational%20Logic%20Design-24.png)

> 有向无环赋权图 [Activity On Vertex Network (AOV 网)](../../DMPT/notes/05-Graph%20Theory.md #Activity %20On%20Vertex%20Network%20(AOV%20网))

![|500](attachments/03-Combinational%20Logic%20Design-25.png)

> 一个可能都应对方法：在没有非门的路上加延迟电路以便二者信号同时进入与门