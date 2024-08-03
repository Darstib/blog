---
date: 2024-05-15
tags:
- blog
---
***
之前在 [memset 0](https://mem.ac/about/) 推荐下使用 sunshine+moonlight 串流，在校园网（局域网）的加成下使用平板远程控制电脑，期间我利用到 ipv6 让平板访问到电脑，但是昨天在 **cmd** 中键入 `ipconfig` 发现 ipv6 不见了，这下咋办？
<!-- more -->
如下，在新尝试了一个 vpn 后，ipv 6 不见了
![|450](attachments/Where%20is%20my%20ipv6.png)
搜了半天，直接上 [结果](https://blog.csdn.net/superjunenaruto/article/details/112007151) ：
控制面板进 `网络和 Internet` ，如下
![](attachments/Where%20is%20my%20ipv6-1.png)
在弹出的 **WLAN 状态中点击属性** ，如下图将 `Internet 协议版本6(TCP?IPv6)` 勾选后逐步退出即可
![](attachments/Where%20is%20my%20ipv6-2.png)
> 关于串流其实还没搞明白，可能后面补我的配置过程？（又在挖坑了）