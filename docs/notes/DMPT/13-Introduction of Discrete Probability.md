> [!attention]
>
> 由于信安原改先上概率论部分，我选择也跳一下，先行学习概率论部分

## Random Experiments & Probability Spaces

> [!quote]
> 
> Each element of the **sample space** is assigned a probability which tells us how likely the outcome is to occur when we actually perform the experiment.
> 
> Typically, a **random experiment** consists of drawing a sample of k elements from a set S of cardinality n.

A probability space is a sample space Ω, together with a probability P[ω] (often also denoted as Pr[ω]) for each sample point ω, such that 

-  (Non-negativity): 0 ≤ P[ω] ≤ 1 for all ω ∈ Ω. 

-  (Sum to 1): ∑ ω∈Ω P[ω] = 1, i.e., the sum of the probabilities over all outcomes is 1.

Formally, an event A made of some sample from Ω is just a subset of the sample space Ω, i.e., A ⊆ Ω

For any event A ⊆ Ω, we define the probability of A to be
$$
P[A]=\sum_{\omega \in A}P[\omega]
$$


## Example

对于普通的古典概型大家在高中就已经学习过，不再涉及，这里记录几个比较有意思的例子：

### Birthday Paradox（生日悖论）

比较长，就放张截图，但是结论就是，23 个人中，有两人同一天生日概率就是 50%以上；60 个人中，有两人同一天生日的概率就达到了 99% ! !

![|500](attachments/13-Discrete%20Probability.png)

### The Monty Hall Problem

详细内容可以自行搜索；概括就是：三（A、B、C）选一，在你选择其中一个（假如选择了 A）后我告诉你其他两个中错误的那个（例如是 C），那么你继续选择 A 还是改选 B 呢？

看起来，二者（A、B 似乎并没有区别，毕竟只是将 C 排除了？）

你看看，A 是最开始就选了的，$\frac{1}{3}$ 没跑了；C 已经被排除了，概率肯定是 0；那你看看这个 B 的概率不就是 $\frac{2}{3}$ 嘛。

那无疑，选 B

![|500](attachments/13-Discrete%20Probability-1.png)

有点奇怪，但是……这个条件概率我们会在后面讲解；因为我排除错误的选项这个概率为 1 ，导致了概率的改变。



