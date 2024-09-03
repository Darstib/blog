
## 1. 请在实验报告中详细描述每一步的过程并配有适当的截图和解释，对于仿真设计和上板验证的结果也应当有适当的解释和照片

### 总述

我们的核心模块就是 Controller 和 Core 两个模块，我将主要展示每一类指令某一特定指令的实现。

#### 在 Core 模块中

在 Core.sv 中，我调用了很多模块，如 controller 和 ALU 等模块，以及一些我自己写的模块，如 ImmGen 模块，这些模块的声明都将在附件中一并送至，在此不甚详谈，在下面的说明中可能会提及一些。 

在 Core.sv 中，根据 pc[2] 我们选择收到的 inst 的高/低 32 位作为我们的指令送给 controller 译码，并初步解析必要字段，如 _opcode_ ，以便后面对特殊信号的处理。 

![|500](attachments/project_report-16.png)
#### 在 controller 中

先决定是什么类型的指令

![|500](attachments/project_report-11.png)

再生成控制信号，首先设置默认信号：

![|500](attachments/project_report-12.png)
### 实现 R Type 的基本数据通路（通过测试 rtype.hex，累计可获得实验部分 10% 的分数）

    - add, sub, sll, slt, sltu, xor, srl, sra, or, and

只需要改变 **alu_op** ，其余信号使用默认值：

![|500](attachments/project_report-13.png)

`make TESTCASE=itype` 

![|500](attachments/project_report-1.png)

### 实现 I Type 的基本数据通路（通过测试 itype.hex，累计可获得实验部分 20% 的分数）

    - addi, slti, sltiu, xori, ori, andi, slli, srli, srai
    - ld

![|500](attachments/project_report-14.png)

`make TESTCASE=itype` 

![|500](attachments/project_report-2.png)

### 实现 S Type 的基本数据通路（通过测试 stype.hex，累计可获得实验部分 30% 的分数）

    - sd

![|500](attachments/project_report-15.png)

`make TESTCASE=stype` 

![|500](attachments/project_report-7.png)

### 实现 B Type 的完整数据通路（通过测试 btype.hex，累计可获得实验部分 40% 的分数）

    - beq, bne, blt, bge, bltu, bgeu

注意 `is_b` 来控制 _npc_sel_ 信号，其中 cmp_res 应该等同于实验指导中的 _br_taken_

![](attachments/project_report-20.png)

`make TESTCASE=btype` 

![|500](attachments/project_report-3.png)
 
### 实现 U Type 的完整数据通路（通过测试 utype.hex，累计可获得实验部分 50% 的分数）

    - lui, auipc

![|500](attachments/project_report-21.png)

二者只在 `alu_asel` 处有所不同，其实可以合而为 1 ，但是相差无几。

`make TESTCASE=utype` 

![|500](attachments/project_report-6.png)

### 实现 J Type 的完整数据通路（通过测试 jtype.hex，累计可获得实验部分 60% 的分数）

    - jal

比较需要注意的是判断 `is_j`，确保 _npc_sel_ 能够控制 pc 的正确变化

![](attachments/project_report-20.png) 

`make TESTCASE=jtype` 

![|500](attachments/project_report-5.png)

### 实现剩余指令的完整数据通路（通过测试 remain.hex，累计可获得实验部分 70% 的分数）

    - jalr, lb, lh, lw, lbu, lhu, lwu
    - sb, sh, sw
    - addiw, slliw, srliw, sraiw
    - addw, subw, sllw, srlw, sraw

比较需要值得注意的是对一些些特殊信号的处理，如 `jalr` 的最低位置 0、64 位特殊指令的结果符号扩展，等等

![|500](attachments/project_report-17.png)

`make TESTCASE=remain` 

![|500](attachments/project_report-8.png)

### 实现所有指令的完整数据通路（通过测试 full.hex，累计可获得实验部分 80% 的分数）

没有遇到额外的问题

`make TESTCASE=full` 

![|500](attachments/project_report-9.png)

`make TESTCASE=sample`

![|500](attachments/project_report-10.png)

### 下板验证，累计可获得实验部分 100% 的分数

`make board_sim TESTCASE=full` 后 `make bitstream` 生成比特流，通过结果如下：

![|150](attachments/d427fb94dbaa152e15d677479622f0a.jpg)

## 2. 可以为系统 I 的实验安排、实验内容、实验指导留下任何宝贵的心得体会和建议吗？（不记录分数，纯属用于吐槽，感谢大家为我们的课改贡献一份力量）

在 sys1 的诸多 lab+project 中，我对实验安排的精心设计和周密组织表示衷心的感谢。实验是理论学习的重要补充，它不仅让我们将抽象的概念转化为具体的实践，还锻炼了我们的动手能力和问题解决能力。

总体来说，我认为实验设计比较令我舒适，我清楚太难了大家都不好过，因为老师助教们用于设计实验花费的精力也会极大地增加；太简单了，怎么能够应对后面的 sys2 sys3 呢？

我依旧想要引用 https://csdiy.wiki/ 中描述的一段话：

![|500](attachments/project_report-19.png)

我们同样有代码框、实验指导、对拍器判断对错；我至今都认为在七段数码管上出现自己的学号、在串口接收时出现自己的学号是非常有成就感的事情；更加辛苦的是老师和助教们。

要是  <u>串口那里能够将输入的数字在开发板上即时显示就更棒了</u>，而不是显示收发信息，那个咱也看不懂 🥲。**当然可能难度会较大，仅作希望**。 

基于水平限制，我无法为实验的精进提供更多地帮助了；实验指导中可能出现些许错字，我想那说不定只是助教们写文档的时候也正犯困呢（bushi）。

再次感谢老师助教们的辛勤付出。