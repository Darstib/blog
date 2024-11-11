---
tags:
  - notes
comments: true
dg-publish: true
---
## GCD && LCM

> https://oi-wiki.org/math/number-theory/gcd/

### Euclid algorithm

欧几里得求解最大公因数 gcd(a,b) 的关键在于 $\gcd(a,b)=\gcd(b,a\mathrm{~mod~}b)$，故：

```python title="gcd.py"
def gcd(a, b) -> int:
    if b == 0:
        return a
    return gcd(b, a % b)
```

那么最小公倍数 lcm(a,b) 呢？想想 $gcd(a,b) \times lcm(a,b)=a\times b$ ，解决了。
### Extended Euclidean algorithm

扩展欧几里得算法使用的关键等式和上面相同，推导略去，主要用于求解形如 $ax+by=\gcd(a,b)$ 中的 (x, y) 解。

```python title="exgcd.py"
def Exgcd(a, b) -> tuple: # d, x, y
    if b == 0:
        return a, 1, 0
    d, x, y = Exgcd(b, a % b)
    return d, y, x - (a // b) * y
```

使用 z3 求解器求解所有可能的解：

```python title="exgcd"
from z3 import *
u, v = Ints("u v")
s = Solver()
s.add(u * p + v * q == gcd(p, q))

while s.check() == sat:
    m = s.model()
    print(f"u = {m[u]}, v = {m[v]}")
    assert m[u].as_long() * p + m[v].as_long() * q == gcd(p, q)
    # 添加约束排除当前解
    current_solution = And(u == m[u].as_long(), v == m[v].as_long())
    s.add(Not(current_solution))
```

> [!QUESTION]
>
> 如何使用扩展欧几里得算法求解形如 $a*x \equiv b \pmod{p}$ 中的 x?

> https://devv.ai/search?threadId=e2xqr5fzft34

1. 求 d = gcd(a, p) ，确保 d 为 b 的约数，否则无解；
2. ax' + py' = gcd(a, p)，求 x', y'
3. $ax'*\frac{b}{d}+py'* \frac{b}{d}=d * \frac{b}{d}=b$
4. $x = \frac{x'*b}{d}$

## Quadratic Residues

### 定义

> [!DEFINITION] 
>
> We say that an integer x is a _Quadratic Residue_ if there exists an aa such that $a^2≡x\pmod p$. If there is no such solution, then the integer is a _Quadratic Non-Residue_.
>
> If $a^2=x$ then $(−a)^2=x$. So if x is a quadratic residue in some finite field, then there are always two solutions for a.

当 p 不太大的时候，我们只要遍历 (0, p-1) 即可：

```python title="quadratic_residues.py"
p = 29
ints = [14, 6, 11]

qr = [a for a in range(p) if pow(a,2,p) in ints]
print(f"flag {min(qr)}")
```

### 使用 sympy

```python title="sqrt_mod"
from sympy import *
# a^2 = x (mod p)
print(sqrt_mod(x, p))
```

### 数学推导求解

![](attachments/Math%20in%20crypto.png)

> https://math.stackexchange.com/questions/1273690/when-p-3-pmod-4-show-that-ap1-4-pmod-p-is-a-square-root-of-a

1. 当 p%4=3 时，$(a^{(p+1)/4})^2\equiv a\pmod{p}$ 。 
2. tonelli_shanks 算法

```python title="tonelli_shanks"
# 代码来自 https://devv.ai/search?threadId=dxl1i5f103r4
def tonelli_shanks(n, p):
    # Step 1: Check if n is a quadratic residue modulo p
    if pow(n, (p - 1) // 2, p) != 1:
        return None  # No solution exists

    # Step 2: Factor p - 1
    Q, S = p - 1, 0
    while Q % 2 == 0:
        Q //= 2
        S += 1

    # Step 3: Find a quadratic non-residue z
    z = 2
    while pow(z, (p - 1) // 2, p) == 1:
        z += 1

    # Step 4: Initialize variables
    M = S
    c = pow(z, Q, p)
    t = pow(n, Q, p)
    R = pow(n, (Q + 1) // 2, p)

    # Step 5: Loop until a solution is found
    while t != 0 and t != 1:
        # Find least i such that t^(2^i) = 1
        t2i = t
        i = 0
        while t2i != 1:
            t2i = (t2i * t2i) % p
            i += 1

        b = pow(c, 2 ** (M - i - 1), p)
        M = i
        c = (b * b) % p
        t = (t * c) % p
        R = (R * b) % p

    return R if t == 1 else None
```
``

## Euler-totient, Fermat's little theorem

### Euler totient

> https://oi-wiki.org/math/number-theory/euler-totient/

> [!MATH]
>
> 即 $\varphi(n)$，表示的是小于等于 n 且与 n 互质的数的个数。

- $\varphi(n)=n-1$ ；当 n 为质数时
- $n=\Pi^s_{i=1}p_{i}^{k_{i}}\implies \varphi(n)=n*\Pi_{i=1}^s\left( \frac{p_{i}-1}{p_{i}} \right)$
    - $n=p^k\implies\varphi(n)=p^k-p^{k-1}$；当 p 为质数时；
- $\varphi(mn)\varphi(\gcd(m,n))=\varphi(m)\varphi(n)\gcd(m,n)$
- $\varphi(mn)=\varphi(m)\varphi(n)$；当 gcd(m,n)=1 时
    - $\varphi(2n)=\varphi(n)\varphi(2)=\varphi(n)$；当 n 为奇数时

> 也许还有[筛法求欧拉函数](https://oi-wiki.org/math/number-theory/sieve/#%E7%AD%9B%E6%B3%95%E6%B1%82%E6%AC%A7%E6%8B%89%E5%87%BD%E6%95%B0)待看

### Fermat's little theorem

> https://oi-wiki.org/math/number-theory/fermat/

> [!MATH] Fermat's little theorem
>
> If is_prime(p) && gcd(a, p)=1 , 
> 
> then $a^{p-1}\equiv 1\pmod{p}$ namely $a^p\equiv a\pmod{p}$

#### 推论一

对于 p 阶的生成元 g，如果 $g^x\equiv g^y\pmod{p}$ ，那么 $x\equiv y\pmod{p-1}$ 。

#### 推论二 Euler's theorem

$gcd(a, p)=1 \implies a^{\varphi(p)}\equiv 1\pmod{p}$

**扩展欧拉定理：**

$$
\begin{aligned}a^b\equiv\begin{cases}a^{b\mathrm{~mod~}\varphi(m)},&\gcd(a,m)=1,\\a^b,&\gcd(a,m)\neq1,b<\varphi(m),&\pmod m\\a^{(b\mathrm{~mod~}\varphi(m))+\varphi(m)},&\gcd(a,m)\neq1,b\geq\varphi(m).&\end{cases}\end{aligned}
$$

其中式一使用较多。

## Pollard’s ρ algorithm

> https://ljcppp.github.io/mySlides/crypto_2024/site/#/3/18
> 
> https://ctf-wiki.org/crypto/asymmetric/discrete-log/discrete-log/#pohlig-hellman-algorithm

> [!KNOWLEDGE]
>
> **光滑**：即可以因子分解成较小的数的乘积。
> 
> p 光滑也意味着群 $\mathbb{Z}_{p}^*$ 有很多小的子群。

所以，可以把大群上的离散对数问题转换成易求的子群上的离散对数问题，最后组合起来。

