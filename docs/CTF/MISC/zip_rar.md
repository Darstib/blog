---
tags:
  - notes
comments: true
dg-publish: true
---

## SWPU 2020

### 套娃

- [nssctf](https://www.nssctf.cn/problem/47)

起初获得一个 “套娃.xls” ，利用 `file` 命令获得是 zip 文件，改扩展名解压，重复一次后获得 RC4data.txt（内容为"U2FsdGVkX19uI2lzmxYrQ9mc16y7la7qc7VTS8gLaUKa49gzXPclxRXVsRJxWz/p"）RC4key.zip（加密） + esayrc4.xlsx（无法打开，修改为 zip 后同样无法打开）。名字提示的这么多了，[了解一下 RC4](https://www.yuxingchen.love/index.php/2024/08/04/rc4%E5%8A%A0%E5%AF%86%E7%AE%97%E6%B3%95%E6%B7%B1%E5%88%BB%E5%89%96%E6%9E%90%E7%BB%93%E5%90%88ctf%E9%80%86%E5%90%91%E7%AD%BE%E5%88%B0/)，得知我们需要密钥/密钥流、密文就可以得到明文。

使用 010 查看文件，在 esayrc4.xlsx [末尾发现了密钥](attachments/zip_rar.png) "ABCDEFGHIJKLMNOPQRSTUVWXYZ" ，放入 [在线rc4网站解密](https://config.net.cn/tools/Rc4.html)[^1]。

[^1]: 这个网站是我在本题的讨论区得知的，其他网站如果要求设置编码格式，解不出来（或者只是没找对），就比较难绷。

> [!FLAG]
>
> NSSCTF{ef1a73d40977a49b99b871980f355757}

## tool