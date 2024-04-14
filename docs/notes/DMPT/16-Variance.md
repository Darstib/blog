## Random Variables: Variance and Covariance

### Variance（方差）

> [!QUOTE]
>
> In [probability theory](https://simple.wikipedia.org/wiki/Probability_theory "Probability theory") and [statistics](https://simple.wikipedia.org/wiki/Statistics "Statistics"), the **variance** is a way to measure how far a [set](https://simple.wikipedia.org/wiki/Set "Set") of numbers is spread out. Variance describes how much a [random variable](https://simple.wikipedia.org/wiki/Random_variable "Random variable") differs from its [expected value](https://simple.wikipedia.org/wiki/Expected_value "Expected value"). The variance is defined as the average of the [squares](https://simple.wikipedia.org/wiki/Square_(mathematics) "Square (mathematics)") of the differences between the individual (observed) and the expected value.

> [!DEFINITION 16.1]
>
> (_Variance_). For a r.v. X with expectation E[X] = µ, the variance of X is defined to be $Var(X) = E[(X − µ)^{2}]$ . The square root $σ(X) := \sqrt{ Var(X) }$ is called the standard deviation of X.

> [!THEOREM 15.3]
>
> For a r.v. X with expectation E[X] = µ, we have $Var(X) = E[X^{2}]-\mu^{2}$ .
> and $Var[cX] = c^{2}Var[X]$ .
>
> and we can even get that:
>
> ![](attachments/15-Distribution%20and%20Expectation-3.png)

### Covariance

> [!DEFINITION 16.2]
>
> (_Covariance_). The covariance of random variables X and Y , denoted Cov(X,Y), is defined as 
> 
> $$Cov(X,Y) = E[(X − \mu_{X} )(Y − \mu_{Y} )] = E[XY]−\mu_{X}\mu_{Y}$$ 
> 
> where µX = E[X] and µY = E[Y].

> [!DEFINITION 16.3]
>
> (_Correlation_). Suppose X and Y are random variables with σ(X) > 0 and σ(Y) > 0. Then, the correlation of X and Y is defined as 
> 
> $$Corr(X, Y) = \frac{Cov(X, Y)}{\sigma(X)\sigma(Y)} \in [-1, 1]$$

看到这里，其实已经可以回忆起高中学习的线性规划了。