---
title: crypto 常用工具
url: https://lazzzaro.github.io/2020/05/10/crypto-crypto%E5%B8%B8%E7%94%A8%E5%B7%A5%E5%85%B7/#Sage
publishedTime: 2020-05-10T14:41:00.000Z
---

> 转载自 [crypto常用工具](https://lazzzaro.github.io/2020/05/10/crypto-crypto%E5%B8%B8%E7%94%A8%E5%B7%A5%E5%85%B7) ，主要是为了留存本地笔记。

#### []( #gmpy2 "gmpy2")gmpy2

<table><tbody><tr><td class="gutter"><pre><span class="line">1</span><br><span class="line">2</span><br><span class="line">3</span><br><span class="line">4</span><br><span class="line">5</span><br><span class="line">6</span><br><span class="line">7</span><br><span class="line">8</span><br><span class="line">9</span><br><span class="line">10</span><br></pre></td><td class="code"><pre><span class="line"><span class="keyword">from</span> gmpy2 <span class="keyword">import</span> *</span><br><span class="line"></span><br><span class="line">mpz(n)	<span class="comment">#初始化一个大整数</span></span><br><span class="line">mpfr(x)	<span class="comment"># 初始化一个高精度浮点数x</span></span><br><span class="line">d = invert(e,n) 	<span class="comment"># 求逆元，de = 1 mod n</span></span><br><span class="line">c = powmod(m,e,n)	<span class="comment"># 幂取模，结果是 c = m^e mod n</span></span><br><span class="line">is_prime(n)	 <span class="comment">#素性检测</span></span><br><span class="line">gcd(a,b)  	<span class="comment">#欧几里得算法 ，最大公约数</span></span><br><span class="line">gcdext(a,b)  	<span class="comment">#扩展欧几里得算法</span></span><br><span class="line">iroot(x,n) 	<span class="comment">#x开n次根</span></span><br></pre></td></tr></tbody></table>

​

#### []( #sympy "sympy")sympy

<table><tbody><tr><td class="gutter"><pre><span class="line">1</span><br><span class="line">2</span><br><span class="line">3</span><br><span class="line">4</span><br><span class="line">5</span><br><span class="line">6</span><br><span class="line">7</span><br><span class="line">8</span><br></pre></td><td class="code"><pre><span class="line"><span class="keyword">from</span> sympy <span class="keyword">import</span> *</span><br><span class="line"></span><br><span class="line">prime(n)  <span class="comment">#第n个素数</span></span><br><span class="line">isprime(n)  <span class="comment">#素性检测</span></span><br><span class="line">primepi(n)  <span class="comment">#小于n的素数的总数</span></span><br><span class="line">nextprime(n)  <span class="comment">#下一个素数</span></span><br><span class="line">prevprime(n)  <span class="comment">#上一个素数</span></span><br><span class="line">nthroot_mod(c,e,p,all_roots=<span class="literal">True</span>)  <span class="comment">#有限域开方</span></span><br></pre></td></tr></tbody></table>

​

#### []( #Sage "Sage")Sage

**定义**

<table><tbody><tr><td class="gutter"><pre><span class="line">1</span><br><span class="line">2</span><br><span class="line">3</span><br><span class="line">4</span><br><span class="line">5</span><br><span class="line">6</span><br><span class="line">7</span><br><span class="line">8</span><br><span class="line">9</span><br></pre></td><td class="code"><pre><span class="line">R.&lt;X&gt; = PolynomialRing(Zmod(n))</span><br><span class="line"><span class="comment">#Zmod (n):指定模，定义界限为 n 的环；Z 表示整数；指定模是划定这个环的界限，就是有效的数字只有从 0 到 n，其他的都通过与 n 取模来保证在 0～n 这个范围内；Zmod 代表这是一个整数域中的 n 模环</span></span><br><span class="line"><span class="comment">#ZZ ：整数环；QQ：有理数环；RR：实数环；CC：复数环</span></span><br><span class="line"><span class="comment">#R ：只是一个指针，指向用 polynomialring 指定的那个环（可以使用任意字符）</span></span><br><span class="line"><span class="comment">#PolynomialRing ：这个就是说建立多项式环</span></span><br><span class="line"><span class="comment">#.&lt;X&gt;：指定一个变量的意思（可以用任意字符）</span></span><br><span class="line"></span><br><span class="line">R.&lt;M&gt; = PolynomialRing(MatrixSpace(Zmod(n),<span class="number">3</span>,<span class="number">3</span>))</span><br><span class="line"><span class="comment">#定义一个模n的矩阵</span></span><br></pre></td></tr></tbody></table>

​

**数论**

<table><tbody><tr><td class="gutter"><pre><span class="line">1</span><br><span class="line">2</span><br><span class="line">3</span><br><span class="line">4</span><br><span class="line">5</span><br><span class="line">6</span><br><span class="line">7</span><br><span class="line">8</span><br><span class="line">9</span><br><span class="line">10</span><br><span class="line">11</span><br><span class="line">12</span><br><span class="line">13</span><br><span class="line">14</span><br><span class="line">15</span><br><span class="line">16</span><br><span class="line">17</span><br><span class="line">18</span><br><span class="line">19</span><br><span class="line">20</span><br><span class="line">21</span><br></pre></td><td class="code"><pre><span class="line">prime_pi(n)  <span class="comment">#小于等于n的素数个数</span></span><br><span class="line">divisors(n)  <span class="comment">#n的因子</span></span><br><span class="line">number_of_divisors(n)  <span class="comment">#n的因子数</span></span><br><span class="line">factor(n)  <span class="comment">#n的因式分解</span></span><br><span class="line">euler_phi(n)  <span class="comment">#n的欧拉函数值</span></span><br><span class="line">two_squares(n)   <span class="comment">#n的两数平方组合</span></span><br><span class="line">three_squares(n)  <span class="comment">#n的三数平方组合</span></span><br><span class="line">four_squares(n)  <span class="comment">#n的四数平方组合</span></span><br><span class="line"></span><br><span class="line">x.nth_root(n, truncate_mode=<span class="literal">True</span>) <span class="comment">#x开n次方 （不管是否完全开方，取整）</span></span><br><span class="line">mod(x,p).nth_root(n) <span class="comment">#x有限域开n次方</span></span><br><span class="line"></span><br><span class="line"><span class="comment"># x有限域开n次方，e大</span></span><br><span class="line"><span class="keyword">def</span> <span class="title function_">mod_nth_root</span>(<span class="params">x, e, n</span>):</span><br><span class="line">    r, z = pari(<span class="string">f"r = sqrtn(Mod(<span class="subst">{x}</span>, <span class="subst">{n}</span>), <span class="subst">{e}</span>, &amp;z); [lift(r), lift(z)]"</span>)</span><br><span class="line">    r, z = <span class="built_in">int</span>(r), <span class="built_in">int</span>(z)</span><br><span class="line">    roots = [r]</span><br><span class="line">    t = r</span><br><span class="line">    <span class="keyword">while</span> (t := (t*z) % n) != r:</span><br><span class="line">        roots.append(t)</span><br><span class="line">    <span class="keyword">return</span> roots</span><br></pre></td></tr></tbody></table>

​

**多项式**

<table><tbody><tr><td class="gutter"><pre><span class="line">1</span><br><span class="line">2</span><br><span class="line">3</span><br><span class="line">4</span><br><span class="line">5</span><br><span class="line">6</span><br><span class="line">7</span><br><span class="line">8</span><br><span class="line">9</span><br><span class="line">10</span><br><span class="line">11</span><br><span class="line">12</span><br><span class="line">13</span><br><span class="line">14</span><br><span class="line">15</span><br><span class="line">16</span><br><span class="line">17</span><br><span class="line">18</span><br><span class="line">19</span><br><span class="line">20</span><br><span class="line">21</span><br><span class="line">22</span><br><span class="line">23</span><br><span class="line">24</span><br><span class="line">25</span><br><span class="line">26</span><br><span class="line">27</span><br><span class="line">28</span><br><span class="line">29</span><br><span class="line">30</span><br><span class="line">31</span><br><span class="line">32</span><br><span class="line">33</span><br><span class="line">34</span><br><span class="line">35</span><br><span class="line">36</span><br><span class="line">37</span><br><span class="line">38</span><br><span class="line">39</span><br><span class="line">40</span><br><span class="line">41</span><br></pre></td><td class="code"><pre><span class="line">f.subs({x:x1}) <span class="comment">#把x1值代入x</span></span><br><span class="line">f.univariate_polynomial() <span class="comment">#映射为单变量多项式</span></span><br><span class="line">f.univariate_polynomial().roots() <span class="comment">#单变量多项式求根</span></span><br><span class="line">f.coefficients() <span class="comment">#多项式系数列表</span></span><br><span class="line">f.padded_list(n) <span class="comment">#多项式系数转换为长度为n的列表</span></span><br><span class="line">f.<span class="built_in">list</span>() <span class="comment">#多项式系数</span></span><br><span class="line">f.monic() <span class="comment">#首一多项式</span></span><br><span class="line">f.sub(x,x-<span class="number">1</span>) <span class="comment">#将x -1 代入 x</span></span><br><span class="line">f.factor() <span class="comment">#分解因式</span></span><br><span class="line"></span><br><span class="line"><span class="comment">#因式分解 （单元）</span></span><br><span class="line">x = PolynomialRing(RationalField(), <span class="string">'x'</span>).gen()</span><br><span class="line">f = (x^<span class="number">3</span> - <span class="number">1</span>)^<span class="number">2</span>-(x^<span class="number">2</span>-<span class="number">1</span>)^<span class="number">2</span></span><br><span class="line">f.factor()</span><br><span class="line"></span><br><span class="line"><span class="comment">#因式分解 （二元）</span></span><br><span class="line">x, y = PolynomialRing(RationalField(), <span class="number">2</span>, [<span class="string">'x'</span>,<span class="string">'y'</span>]).gens()</span><br><span class="line">f =  (<span class="number">9</span>*y^<span class="number">6</span> - <span class="number">9</span>*x^<span class="number">2</span>*y^<span class="number">5</span> - <span class="number">18</span>*x^<span class="number">3</span>*y^<span class="number">4</span> - <span class="number">9</span>*x^<span class="number">5</span>*y^<span class="number">4</span> + <span class="number">9</span>*x^<span class="number">6</span>*y^<span class="number">2</span> + <span class="number">9</span>*x^<span class="number">7</span>*y^<span class="number">3</span> + <span class="number">18</span>*x^<span class="number">8</span>*y^<span class="number">2</span> - <span class="number">9</span>*x^<span class="number">11</span>)</span><br><span class="line">f.factor()</span><br><span class="line"></span><br><span class="line"><span class="comment">#GCD （单元）</span></span><br><span class="line">x = PolynomialRing(RationalField(), <span class="string">'x'</span>).gen()</span><br><span class="line">f = <span class="number">3</span>*x^<span class="number">3</span> + x</span><br><span class="line">g = <span class="number">9</span>*x*(x+<span class="number">1</span>)</span><br><span class="line">f.gcd(g)</span><br><span class="line"></span><br><span class="line"><span class="comment">#GCD （多元）</span></span><br><span class="line">R.&lt;x,y,z&gt; = PolynomialRing(RationalField(), order=<span class="string">'lex'</span>)</span><br><span class="line">f = <span class="number">3</span>*x^<span class="number">2</span>*(x+y)</span><br><span class="line">g = <span class="number">9</span>*x*(y^<span class="number">2</span> - x^<span class="number">2</span>)</span><br><span class="line">f.gcd(g)</span><br><span class="line"></span><br><span class="line"><span class="comment">#多项式/整数转换</span></span><br><span class="line">PR = PolynomialRing(GF(<span class="number">2</span>),<span class="string">'x'</span>)</span><br><span class="line">R.&lt;x&gt; = GF(<span class="number">2</span>^<span class="number">2049</span>)</span><br><span class="line">pc = R.fetch_int(xx) <span class="comment">#整数转多项式</span></span><br><span class="line">xx = R(PR(pc)).integer_representation() <span class="comment">#多项式转整数</span></span><br><span class="line"></span><br><span class="line"><span class="comment">#拉格朗日插值</span></span><br><span class="line">PR = PolynomialRing(Zmod(p), <span class="string">'x'</span>)</span><br><span class="line">f = PR.lagrange_polynomial(points)</span><br></pre></td></tr></tbody></table>

​

**矩阵**

<table><tbody><tr><td class="gutter"><pre><span class="line">1</span><br><span class="line">2</span><br><span class="line">3</span><br><span class="line">4</span><br><span class="line">5</span><br><span class="line">6</span><br><span class="line">7</span><br><span class="line">8</span><br><span class="line">9</span><br><span class="line">10</span><br><span class="line">11</span><br><span class="line">12</span><br><span class="line">13</span><br><span class="line">14</span><br><span class="line">15</span><br><span class="line">16</span><br><span class="line">17</span><br><span class="line">18</span><br><span class="line">19</span><br><span class="line">20</span><br><span class="line">21</span><br></pre></td><td class="code"><pre><span class="line">A = matrix(ZZ, [[<span class="number">1</span>,<span class="number">1</span>],[<span class="number">0</span>,<span class="number">4</span>]])</span><br><span class="line">A.nrows() <span class="comment">#行数</span></span><br><span class="line">A.ncols() <span class="comment">#列数</span></span><br><span class="line">A.transpose() <span class="comment">#转置</span></span><br><span class="line">A.inverse() 或 A^(-<span class="number">1</span>) <span class="comment">#逆</span></span><br><span class="line">A.rank() <span class="comment">#秩</span></span><br><span class="line">A.det() <span class="comment">#行列式</span></span><br><span class="line">A.stack(vector([<span class="number">1</span>,<span class="number">2</span>])) <span class="comment">#矩阵后添加一行</span></span><br><span class="line">A.augment(vector([<span class="number">1</span>,<span class="number">2</span>])) <span class="comment">#矩阵后添加一列</span></span><br><span class="line">A.insert_row(<span class="number">1</span>, vector([<span class="number">1</span>,<span class="number">2</span>])) <span class="comment">#在第一行插入</span></span><br><span class="line">A.change_ring(QQ) <span class="comment">#更换环为QQ</span></span><br><span class="line">A.solve_left(B) 或 A/B <span class="comment">#求解XA =B</span></span><br><span class="line">A.solve_right(B) 或 A\B <span class="comment">#求解AX =B</span></span><br><span class="line">A.left_kernel() <span class="comment">#求解XA =0，线性相关的行向量</span></span><br><span class="line">A.right_kernel() <span class="comment">#求解AX =0，线性相关的行向量</span></span><br><span class="line">A.LLL() <span class="comment">#最短正交基</span></span><br><span class="line">A.multiplicative_order() <span class="comment">#乘法阶</span></span><br><span class="line"></span><br><span class="line">matrix.zero(<span class="number">2</span>,<span class="number">3</span>) / zero_matrix(<span class="number">2</span>,<span class="number">3</span>) <span class="comment">#2 *3 零矩阵</span></span><br><span class="line">matrix.identity(<span class="number">2</span>) / identity_matrix(<span class="number">2</span>) <span class="comment">#2 *2 单位阵</span></span><br><span class="line">block_matrix(QQ,[[A,zero_matrix(n,<span class="number">1</span>)],[matrix(b),matrix([<span class="number">1e-16</span>])]]) <span class="comment">#矩阵拼接</span></span><br></pre></td></tr></tbody></table>

​

**解方程**

{x+y\=10xy\=21

<table><tbody><tr><td class="gutter"><pre><span class="line">1</span><br><span class="line">2</span><br></pre></td><td class="code"><pre><span class="line">var(<span class="string">'x y'</span>)</span><br><span class="line">solve([x+y==<span class="number">10</span>,x*y==<span class="number">21</span>],[x,y])</span><br></pre></td></tr></tbody></table>

​

**解线性方程组**

AX\=B

<table><tbody><tr><td class="gutter"><pre><span class="line">1</span><br><span class="line">2</span><br><span class="line">3</span><br><span class="line">4</span><br><span class="line">5</span><br><span class="line">6</span><br></pre></td><td class="code"><pre><span class="line">A = Matrix([[<span class="number">1</span>,<span class="number">2</span>,<span class="number">3</span>],[<span class="number">3</span>,<span class="number">2</span>,<span class="number">1</span>],[<span class="number">1</span>,<span class="number">1</span>,<span class="number">1</span>]]) </span><br><span class="line">Y = vector([<span class="number">0</span>,-<span class="number">4</span>,-<span class="number">1</span>]) </span><br><span class="line">X = A.solve_right(Y)</span><br><span class="line"><span class="comment">#或</span></span><br><span class="line">A \ Y</span><br><span class="line"><span class="comment">#反斜杠 \ 可以代替 solve_right; 用 A \ Y 代替 A.solve right(Y).</span></span><br></pre></td></tr></tbody></table>

​

**求逆元**

ed\=1(modφ(n))

<table><tbody><tr><td class="gutter"><pre><span class="line">1</span><br></pre></td><td class="code"><pre><span class="line">d = inverse_mod(e,fn) <span class="comment"># sage求逆元</span></span><br></pre></td></tr></tbody></table>

​

**扩展欧几里得算法**

<table><tbody><tr><td class="gutter"><pre><span class="line">1</span><br><span class="line">2</span><br></pre></td><td class="code"><pre><span class="line">d,u,v=xgcd(<span class="number">20</span>,<span class="number">30</span>)</span><br><span class="line"><span class="built_in">print</span>(<span class="string">"d:{0} u:{1} v:{2}"</span>.<span class="built_in">format</span>(d,u,v)) <span class="comment">#d :10 u:-1 v:1</span></span><br></pre></td></tr></tbody></table>

​

**CRT（中国剩余定理）**

{x≡2(mod3)x≡3(mod5)x≡2(mod7)

<table><tbody><tr><td class="gutter"><pre><span class="line">1</span><br><span class="line">2</span><br><span class="line">3</span><br><span class="line">4</span><br><span class="line">5</span><br><span class="line">6</span><br><span class="line">7</span><br><span class="line">8</span><br><span class="line">9</span><br></pre></td><td class="code"><pre><span class="line"><span class="comment">#仅适用模两两互素</span></span><br><span class="line"><span class="keyword">def</span> <span class="title function_">chinese_remainder</span>(<span class="params">modulus, remainders</span>):</span><br><span class="line">    Sum = <span class="number">0</span></span><br><span class="line">    prod = reduce(<span class="keyword">lambda</span> a, b: a*b, modulus)</span><br><span class="line">    <span class="keyword">for</span> m_i, r_i <span class="keyword">in</span> <span class="built_in">zip</span>(modulus, remainders):</span><br><span class="line">        p = prod // m_i</span><br><span class="line">        Sum += r_i * (inverse_mod(p,m_i)*p)</span><br><span class="line">    <span class="keyword">return</span> Sum % prod</span><br><span class="line">chinese_remainder([<span class="number">3</span>,<span class="number">5</span>,<span class="number">7</span>],[<span class="number">2</span>,<span class="number">3</span>,<span class="number">2</span>]) <span class="comment">#23</span></span><br></pre></td></tr></tbody></table>

​

**离散对数**

ax≡b(modn)

<table><tbody><tr><td class="gutter"><pre><span class="line">1</span><br><span class="line">2</span><br><span class="line">3</span><br><span class="line">4</span><br><span class="line">5</span><br><span class="line">6</span><br><span class="line">7</span><br><span class="line">8</span><br><span class="line">9</span><br><span class="line">10</span><br><span class="line">11</span><br></pre></td><td class="code"><pre><span class="line"><span class="comment">#n为合数 （Pohlig-Hellman）</span></span><br><span class="line">x = discrete_log(mod(b,n),mod(a,n)) </span><br><span class="line"></span><br><span class="line"><span class="comment">#n为质数或质数幂 （线性筛 Index Calculus）</span></span><br><span class="line">R = Integers(<span class="number">99</span>)</span><br><span class="line">a = R(<span class="number">4</span>)</span><br><span class="line">b = a^<span class="number">9</span></span><br><span class="line">b.log(a)</span><br><span class="line"></span><br><span class="line">x = <span class="built_in">int</span>(pari(<span class="string">f"znlog(<span class="subst">{<span class="built_in">int</span>(b)}</span>,Mod(<span class="subst">{<span class="built_in">int</span>(a)}</span>,<span class="subst">{<span class="built_in">int</span>(n)}</span>))"</span>))</span><br><span class="line">x = gp.znlog(b, gp.Mod(a, n))</span><br></pre></td></tr></tbody></table>

​

**欧拉函数**

φ(x)\=x∏i\=1n(1−1pi)

<table><tbody><tr><td class="gutter"><pre><span class="line">1</span><br></pre></td><td class="code"><pre><span class="line"><span class="built_in">print</span>(euler_phi(<span class="number">71</span>)) <span class="comment">#70</span></span><br></pre></td></tr></tbody></table>

​

**整数域椭圆曲线**

y2\=x3+a4x+a6

输出所有整数点

<table><tbody><tr><td class="gutter"><pre><span class="line">1</span><br><span class="line">2</span><br><span class="line">3</span><br><span class="line">4</span><br><span class="line">5</span><br><span class="line">6</span><br><span class="line">7</span><br><span class="line">8</span><br><span class="line">9</span><br><span class="line">10</span><br><span class="line">11</span><br><span class="line">12</span><br><span class="line">13</span><br><span class="line">14</span><br><span class="line">15</span><br><span class="line">16</span><br><span class="line">17</span><br><span class="line">18</span><br><span class="line">19</span><br><span class="line">20</span><br></pre></td><td class="code"><pre><span class="line"><span class="comment">#素数域</span></span><br><span class="line">F = GF(<span class="number">7</span>)</span><br><span class="line"><span class="comment">#素数域的阶</span></span><br><span class="line"><span class="built_in">print</span>(F.order())</span><br><span class="line"><span class="comment">#椭圆曲线E7 (2,3)</span></span><br><span class="line">E = EllipticCurve(F,[<span class="number">0</span>,<span class="number">0</span>,<span class="number">0</span>,<span class="number">2</span>,<span class="number">3</span>])</span><br><span class="line"><span class="comment">#基点坐标</span></span><br><span class="line">G = E.gens()[<span class="number">0</span>]</span><br><span class="line"><span class="comment">#阶 （不同的离散的点个数）</span></span><br><span class="line">q = E.order()</span><br><span class="line"><span class="comment">#所有的点</span></span><br><span class="line">allPoints = E.points()</span><br><span class="line"><span class="comment">#创建点</span></span><br><span class="line">P = E(<span class="number">2</span>,<span class="number">1</span>)</span><br><span class="line"><span class="comment">#点的xy坐标值</span></span><br><span class="line">P.xy()</span><br><span class="line"></span><br><span class="line"><span class="comment">#倍数点</span></span><br><span class="line">Q = k*P</span><br><span class="line">Q.division_points(k) <span class="comment"># 结果为P</span></span><br></pre></td></tr></tbody></table>

​

**曲线**

<table><tbody><tr><td class="gutter"><pre><span class="line">1</span><br><span class="line">2</span><br><span class="line">3</span><br><span class="line">4</span><br><span class="line">5</span><br><span class="line">6</span><br><span class="line">7</span><br><span class="line">8</span><br><span class="line">9</span><br><span class="line">10</span><br><span class="line">11</span><br><span class="line">12</span><br><span class="line">13</span><br></pre></td><td class="code"><pre><span class="line"><span class="comment"># 查亏格（Genus）</span></span><br><span class="line">x, y = ZZ[<span class="string">'x, y'</span>].gens()</span><br><span class="line">eq = x ^ <span class="number">3</span> + y ^ <span class="number">3</span> + <span class="number">1</span> - d * x * y</span><br><span class="line">Curve(eq).genus() <span class="comment"># Genus=1为椭圆曲线</span></span><br><span class="line"></span><br><span class="line"><span class="comment"># 映射</span></span><br><span class="line"><span class="comment"># solve x^3+y^3+z^3=d*x*y*z</span></span><br><span class="line">R.&lt;xx,yy,zz&gt; = Zmod(p)[]</span><br><span class="line">cubic = xx^<span class="number">3</span> + yy^<span class="number">3</span> + zz^<span class="number">3</span> - d * xx * yy * zz</span><br><span class="line">EC = EllipticCurve_from_cubic(cubic, morphism=<span class="literal">False</span>) <span class="comment">#映射的椭圆曲线</span></span><br><span class="line">mf = EllipticCurve_from_cubic(cubic, morphism=<span class="literal">True</span>) <span class="comment">#映射关系</span></span><br><span class="line">P = </span><br><span class="line">PP = mf(P)</span><br></pre></td></tr></tbody></table>

​

**解模方程**

ax2+bx+c≡d(modp)

<table><tbody><tr><td class="gutter"><pre><span class="line">1</span><br><span class="line">2</span><br><span class="line">3</span><br><span class="line">4</span><br></pre></td><td class="code"><pre><span class="line">P.&lt;x&gt; = PolynomialRing(Zmod(p))</span><br><span class="line">f = a * x^<span class="number">2</span> + b * x + c - d</span><br><span class="line">x = f.monic().roots()</span><br><span class="line"><span class="built_in">print</span>(x)</span><br></pre></td></tr></tbody></table>

​

**解方程组**

{N\=pqφ\=(p−1)(q−1)

<table><tbody><tr><td class="gutter"><pre><span class="line">1</span><br><span class="line">2</span><br><span class="line">3</span><br><span class="line">4</span><br><span class="line">5</span><br><span class="line">6</span><br><span class="line">7</span><br><span class="line">8</span><br><span class="line">9</span><br><span class="line">10</span><br><span class="line">11</span><br><span class="line">12</span><br><span class="line">13</span><br><span class="line">14</span><br><span class="line">15</span><br><span class="line">16</span><br></pre></td><td class="code"><pre><span class="line">P.&lt;p, q&gt; = PolynomialRing(ZZ)</span><br><span class="line"><span class="keyword">def</span> <span class="title function_">solve</span>(<span class="params">f1, f2</span>):</span><br><span class="line">	g = f1.resultant(f2, q)</span><br><span class="line">	roots = g.univariate_polynomial().roots()</span><br><span class="line">	<span class="keyword">if</span> <span class="built_in">len</span>(roots) == <span class="number">0</span>:</span><br><span class="line">		<span class="keyword">return</span> <span class="literal">False</span></span><br><span class="line">	p_ = <span class="built_in">abs</span>(roots[<span class="number">0</span>][<span class="number">0</span>])</span><br><span class="line">	q_ = <span class="built_in">abs</span>(roots[<span class="number">1</span>][<span class="number">0</span>])</span><br><span class="line">	<span class="keyword">return</span> (<span class="built_in">min</span>(p_, q_), <span class="built_in">max</span>(p_, q_))</span><br><span class="line"></span><br><span class="line">N = </span><br><span class="line">phi = </span><br><span class="line">f1 = (N + <span class="number">1</span>) - phi - p - q</span><br><span class="line">f2 = N - p*q</span><br><span class="line">p, q = solve(f1, f2)</span><br><span class="line">(p, q)</span><br></pre></td></tr></tbody></table>

参考：

[https://jayxv.github.io/2020/05/20/sage%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4/](https://jayxv.github.io/2020/05/20/sage%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4/)

​

**结式**

<table><tbody><tr><td class="gutter"><pre><span class="line">1</span><br><span class="line">2</span><br><span class="line">3</span><br><span class="line">4</span><br><span class="line">5</span><br><span class="line">6</span><br><span class="line">7</span><br><span class="line">8</span><br><span class="line">9</span><br><span class="line">10</span><br><span class="line">11</span><br><span class="line">12</span><br><span class="line">13</span><br></pre></td><td class="code"><pre><span class="line"><span class="keyword">from</span> sage.matrix.matrix2 <span class="keyword">import</span> Matrix</span><br><span class="line"><span class="keyword">def</span> <span class="title function_">resultant</span>(<span class="params">f1, f2, var</span>):</span><br><span class="line">    <span class="keyword">return</span> Matrix.determinant(f1.sylvester_matrix(f2, var))</span><br><span class="line"></span><br><span class="line">n = </span><br><span class="line">P.&lt;k,t2,t3,d&gt; = PolynomialRing(Integers(n))</span><br><span class="line">f1 = s1*k - h - r*d</span><br><span class="line">f2 = s2*(k+t2) - h - r*d</span><br><span class="line">f3 = s3*(k+t3) - h - r*d</span><br><span class="line">h1 = resultant(f1, f2, d)</span><br><span class="line">h2 = resultant(f1, f3, d)</span><br><span class="line">g1 = resultant(h1, h2, k)</span><br><span class="line">roots = g1.univariate_polynomial().roots()</span><br></pre></td></tr></tbody></table>

​

+   #### []( #WolframAlpha "WolframAlpha")WolframAlpha
    
    [https://www.wolframalpha.com/](https://www.wolframalpha.com/)
