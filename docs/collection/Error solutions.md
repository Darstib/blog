---
date: 2024-07-22
tags:
- collection
- blog
---
***
一些杂七杂八的解决问题小记；因为确实挺杂的，全单独开一篇博客多奇怪；我也在思考如何保存比较合适，
<!-- more -->
###### Fail to sign in when using Copilot on vscode
> 在更换学生认证包后，vscode 上的 copilot 突然间登入不上，体现在点击登陆后自动跳转到认证界面，确定后 vscode 这边却没反应。
搜索后有人指向了 setting.json，打开搜索，确实发现了：
```json
"github.copilot.chat.localeOverride": "zh-CN",
"github.copilot.preferredAccount": "...",  // 此处省略我的 GitHub 邮箱地址
"github.copilot.enable": {
  "*": true,
  "plaintext": false,
  "markdown": false,
  "scminput": false
},
```
尝试删除后重试，问题解决；建议 Ctrl x 剪切，万一问题不在这，也能复原。
###### 怎么看谁给某一 GitHub 项目 star ?
[Devv 的回答](https://devv.ai/search?threadId=dtl3co7b1a0w)
###### ipv6 不见了？
[Where is my ipv6](posts/Where%20is%20my%20ipv6.md)
###### 连上 wifi 但是没有用？
[Why I connect wifi but can't use it ?](../../posts/)
###### obsidian 文件保存失败？
[Fail to save files](https://forum.obsidian.md/t/failed-to-save-a-file-eperm-operation-not-permitted/33760/4)
###### change version of GCC in WSL
https://blog.csdn.net/qq_39779233/article/details/105124478
https://lindevs.com/install-gcc-on-ubuntu/