---
tags:
  - notes
comments: true
dg-publish: true
---

## 课堂 PPT 测试题

### 静电学 II

---

![|350](attachments/physics2-problems.png)
![|350](attachments/physics2-problems-1.png)

![|500](attachments/physics2-problems-2.png)

---

> [!QUESTION]
>
> 一块面积为 S 的金属大薄平板 A，带电量为 Q，在其附近平行放置另一块不带电的金属大薄平板 B，两板间距远小于板的线度。试求两板表面的电荷面密度，以及周围空间的场强分布。

![](attachments/physics2-problems-3.png)

A/B 内部场强为 0，取向右为正，故有：

$$
\begin{cases}
\frac{\sigma_1}{2\varepsilon_0}-\frac{\sigma_2}{2\varepsilon_0}-\frac{\sigma_3}{2\varepsilon_0}-\frac{\sigma_4}{2\varepsilon_0}=0 \quad A内部 \\ \frac{\sigma_1}{2\varepsilon_0}+\frac{\sigma_2}{2\varepsilon_0}+\frac{\sigma_3}{2\varepsilon_0}-\frac{\sigma_4}{2\varepsilon_0}=0\quad B 内部 
\end{cases}  
$$

![](attachments/physics2-problems-4.png)

---

> [!QUESTION]
>
> 在内外半径分别为 R1 和 R2 的导体球壳内，有一个半径为 r 的导体小球，小球与球壳同心，让小球与球壳分别带上电荷量 q 和 Q。试求：
> 
> ㈠ 小球的电势 Ur，球壳内、外表面的电势；
> ㈡ 两球的电势差；
> ㈢ 若球壳接地，再次求小球与球壳的电势差。

![](attachments/physics2-problems-5.png)

小球整体等势，所以我们求小球中心的电势即可： $U_r=\frac{1}{4\pi\varepsilon_0}(\frac{q}{r}-\frac{q}{R_1}+\frac{q+Q}{R_2})$

对于球壳表面，同样将电势叠加即可：$U_{R_1}=\frac{1}{4\pi\varepsilon_0}(\frac{q}{R_1}-\frac{q}{R_1}+\frac{q+Q}{R_2})=\frac{1}{4\pi\varepsilon_0}\frac{q+Q}{R_2} = U_{R_{2}}$

故电势差为：$U_r-U_{R_1}=\frac1{4\pi\varepsilon_0}(\frac qr-\frac q{R_1})$ 可以发现电势差与 Q 无关

（三） 若球壳接地，外表面电荷为 0，内表面 -q；内外表面电势均为 0；

---

![](attachments/physics2-problems-6.png)

---

![](attachments/physics2-problems-7.png)

由 B 至接地，可以将其看作两个电容器并联：

$$
\begin{aligned}&U_{BA}=U_{BC}\to E_{BA}=2E_{BC}\to q_{B\text{上}}=2q_{B\text{下}}=\frac{2q}{3}\\&q_{A\text{下}}=-q_{B\text{上}}=-\frac{2q}{3},\:q_{C\text{上}}=-q_{B\text{下}}=-\frac{q}{3}\\ & C_{BA}=\varepsilon_0S/d,\:C_{BC}=\varepsilon_0S/2d,\to C=C_{BA}+C_{BC}=3\varepsilon_0S/2d\end{aligned}
$$
---

![](attachments/physics2-problems-8.png)

对于考试而言，把“极化”当作一个“场”，并记住[极化强度是如何影响电荷面密度](attachments/physics2-problems-9.png)的即可。

![](attachments/physics2-problems-10.png)

---

![](attachments/physics2-problems-11.png)

