---
date: 2024-05-12
tags:
  - blog
  - collections
---
***

经常性的会用了某些东西，之后再找太困难了，做笔记写文章没有必要，放书签里又太多了，所以打算集中放在这里，不定期更新。

<!-- more -->

> PS: 分类带有个人主观判断，部分需要魔法，不加标注。

## 在线网站

### AI

#### AGI

> 官网本身就不介绍了，想用就很好搜；只考虑了白嫖情况；同时实话说，能够白嫖的而不限额度的模型，是不是真实标注的那个就不好说了。

- [theb](https://beta.theb.ai/home)
    - 左侧可选免费模型，截至 2024/08/03，包括：Gemma 2 9B/Claude 3 Haiku/Llama 3.1 8B/GPT-4o Mini 等
- [AIGC+](https://hiai.me/chat)
    - 可以免费用 GPT-4o 和 GPT-4o-Mini 的 Free 版本
    - 感觉质量还可以，至于什么是 Free 版本就不好说了
- [POE](https://poe.com/)
    - 可以使用前沿大模型，每天 3000 积分
        - **GPT-4o-Mini 15/次**
        - GPT-4o 300/次
        - Claude-3.5-Sonnet 200/次
    - 当然还有其他模型，自查
- [monica](https://monica.im/home)
    - 可以免费使用 GPT-4o-Mini 40 次/天
- [huggingface](https://huggingface.co/)
    - 收集了众多开源大模型
    - 目前最好的应该是 meta-llama/Meta-Llama-3.1-405B-Instruct-FP8 ？
- [ai sdk](https://sdk.vercel.ai/playground)
    - 类上，可以免费使用一些开源大模型
- [Coze](https://www.coze.com/home)
    - 国内叫扣子，本来是白嫖神器，后来限额太严重了，个人放弃
- [midjourny 中国站](https://www.midjourny.cn/)
#### 搜索

- [Devv](https://devv.ai/zh)
    - “最懂程序员的新一代 AI 搜索引擎”
    - 基于国外搜索引擎，适合问答
- [metaso](https://metaso.cn/)
    - 基于国内搜索引擎，适合梳理

### 读/写文章

#### 读

比较多的是在 arxiv 的论文，所以也专门找了一下：

- [GPT 学术优化 (GPT Academic)](https://github.com/binary-husky/gpt_academic)
    - 比较厉害的一个功能是，根据 arxiv 论文**摘要链接**，获取 tex 源码，对其翻译后再编译，所以翻译后看起来比直接翻译 pdf 好很多!！
        - 需要是摘要链接，举个例子：https://arxiv.org/abs/2407.21566；同时需要作者上传了 tex 源码，否则无法获取
    - 基于本地部署较麻烦
    - [学术版GPT 网页非盈利版](https://academic.chatwithpaper.org/)
        - 算是一个便携版，个人使用款。
        - 针对 arxiv:
            - 使用 GPT-4o mini 模型，比较快，暂时不知道有没有限制；
            - 产出中可能有乱码，merge_translate_zh 版本的 pdf 效果较好；
            - 如果出现失败可以尝试在浏览器隐私模式下再试（原因原作者也不详）；
            - [这里 -> zh_Traced ICSE 24](../static/zh_Traced%20ICSE%2024.pdf){:download="zh_Traced ICSE 24"} 是一个成功例子。
        - 针对其他 pdf:
            - 尝试 PDF2PDF 功能，[教程](https://zhuanlan.zhihu.com/p/692337102)。
    - [ZJU翻版](https://academic.zchat.tech/)
        - [API 获取](https://zchat.tech/users/setting)
        - 仍然需要 tex 编译环境，个人未使用。
- - [沉浸式翻译](https://chromewebstore.google.com/detail/%E6%B2%89%E6%B5%B8%E5%BC%8F%E7%BF%BB%E8%AF%91-%E7%BD%91%E9%A1%B5%E7%BF%BB%E8%AF%91%E6%8F%92%E4%BB%B6-pdf%E7%BF%BB%E8%AF%91-%E5%85%8D%E8%B4%B9/bpoadfkcbjbfhfodiogcnhhhpibjhbnh)
    - 浏览器插件，阅读 html 版本的可以直接翻译。
- [Readpaper](https://readpaper.com/home/)
    - [B站介绍视频](https://www.bilibili.com/video/BV1dg411P7De/?vd_source=0a037c4dd2becee04d2b1ccafdc1862e)
    - 有一定的 paper，上面带的全文翻译还不错。
- [txyz](https://app.txyz.ai/)
    - 配置 ai 的论文阅读器；
    - 不支持做标记，不支持直接选段分析；
    - 比较适合帮助理解文章？

#### 写

- [typst]() 
    - 如果只是想写一个好看的 pdf ，typst 的成本远低于 latex
    - 这里是一个简单的入门指南 [Make pdf with typst](posts/Make%20pdf%20with%20typst.md)
- [latex](https://www.latex-project.org/) 
    - 个人还是觉得 latex 太麻烦了，在其他地方写写数学公式就得了，配置环境真是难受；
    - 这里是一个很好的[教程文件](https://www.cnblogs.com/eslzzyl/p/17358405.html)；
    - 不得不吐槽一下 latex 的 **庞大**；但是基于 latex 延续已久而模板颇多，暂不能抛弃
    - [这里](https://www.cnblogs.com/eslzzyl/p/17358405.html#:~:text=Enter%20command%3A-,%E8%B0%83%E6%95%B4%E5%AE%89%E8%A3%85%E9%85%8D%E7%BD%AE,-%E8%BF%99%E4%B8%80%E8%8A%82%E6%98%AF) 丢弃了很多暂不需要的宏包，如果以后需要再重新安装
        - 【更新】如果是经常使用一些其他人的模板或者还是书写论文等，还是装了比较好
        - 重新安装宏包花了一番功夫，好在找到了 [这个](https://askubuntu.com/questions/1206440/tlmgr-not-found-when-run-as-root) [这个](https://tex.stackexchange.com/questions/341789/tlmgr-packages-not-present-in-repository)

### 知识学习

#### 编程

- [hello-algo](https://www.hello-algo.com/)
    - 适合初学者的算法学习平台
    - 比较可惜发现时 FDS 已经上完了，属于是半吊子水平，但很难给出时间系统学习算法了
- [LeetCode 算法通关指南](https://algo.itcharge.cn/)
    - 类上，附带在 LeetCode 上的题；但是只讲了 python
- [leetcode_problem_rating](https://zerotrac.github.io/leetcode_problem_rating/#/)
    - [zerotrac](https://github.com/zerotrac) 对于部分 LeetCode 题的排序，由难到容易，适合刷题入门

#### 自学指南

- [CS 自学指南](https://csdiy.wiki/)
    - “是一份献给北大信科学弟学妹们的礼物。”
    - [HDU 版](https://hdu-cs.wiki/)
        - 适合（相比于北京大学学子）水平更低的同学
        - 如果是刚接触 CS 的同学，非常推荐，有很多确实是我个人摸索了一年才逐渐发现的东西，有点后悔没能早点发现
        - [上海交通大学生存手册](https://survivesjtu.gitbook.io/survivesjtumanual)
- [zju-cs-asio](https://isshikihugh.github.io/zju-cs-asio/)
    - ZJU “老一辈”的课程笔记
    - [实用技能拾遗](https://slides.tonycrane.cc/PracticalSkillsTutorial/)
    - [图灵班学习指南](https://zju-turing.github.io/TuringCourses/)
    - 推荐阅读
        - [实用工具推荐](https://turing2024.tonycrane.cc/tools/)
        - [成为一个合格的 CS 人](https://turing2024.tonycrane.cc/cser/)
- [OI wiki](https://oi-wiki.org/)
    - “**OI Wiki** 致力于成为一个免费开放且持续更新的 **编程竞赛（competitive programming）** 知识整合站点”。
    - [数模百科](https://modelwiki.cn/wiki)
    - [数理百科](https://wuli.wiki/index.html)
- [编程导航](https://www.code-nav.cn/course?learnCondition=0&sortField=priority)
    - 鱼皮做的的一个交流平台
- https://teachyourselfcs.com/

#### 一些平台

- https://sagecell.sagemath.org./
    - sagemath 官方在线编译器
- [online compiler](https://godbolt.org/)
    - 免费“代码床”，因为右上角 **share** 可以获得 <u>保留代码</u> 的链接
    - 在线编辑器，可以同时切换编译器运行代码
- [Json](https://www.json.cn/)
- [explainshell](https://explainshell.com/)
    - 帮你读懂 shell 指令
- [编程词典](https://dict.code-nav.cn/)
    - 帮你系统了解某一门语言需要了解哪些专业术语
    - 以工作为目的，不具备搜索功能 ~~但是不会还有人不会用你的搜索引擎搜索特定网站吧~~
- [清华大学开源软件镜像站](https://mirrors.tuna.tsinghua.edu.cn/)
- [浙江大学开源软件镜像站](https://mirror.zju.edu.cn/)

#### 效率提高

- [geogebra](https://www.geogebra.org/)
    - 一套免费的数学工具
- [wolframalpha](https://www.wolframalpha.com/)
- [mathdf](https://mathdf.com/)
- [graph_editor](https://csacademy.com/app/graph_editor)
    - 图论中的作图工具
- [excalidraw](https://excalidraw.com/)
    - 感觉比较适合画结构图；
    - 自己还没用过，但是见过有人使用过，感觉不错
- [processon](https://www.processon.com/)
    - 免费在线流程图思维导图
- [vim_learning](https://vimawesome.com/)
    - 属于是分享但是自己还没用过(bushi)

### 文件类

#### 文档（PDF 为主）

- 免费在线文档转换，pdf操作
    - [ILovePdf](https://www.ilovepdf.com/)
    - [XPdf](https://xpdf.cn)
- [离线转换器](https://offlineconverter.com/cn/)
- [pandoc](https://pandoc.org/)
    - a universal document converter

#### 图片

- [imgbb](https://imgbb.com/)
    - 免费图床

#### 视频

- [123APPS](https://online-video-cutter.com/cn/)
    - 支持视频/音频/PDF 操作；
    - 但是个人目前只是用过编辑视频，其他功能未尝试。

> 下面主要是视频在线下载网站，总有这个网站无效另一个有效的情况，所以留下几个比较好用的，功能上具有重复性。

- [SaveTheVideo](https://www.savethevideo.com/home)
    - 个人主要使用，感觉除了 Youtube 都支持。
- [Save](https://save.tube/)
    - 主要用于 youtube 视频下载
- [ssyoutube](https://ssyoutube.com/en778EN/)
- [SnapAny](https://snapany.com/zh)
    - 理论支持[哔哩哔哩](https://snapany.com/zh/bilibili) [TikTok](https://snapany.com/zh/tiktok) [Pinterest](https://snapany.com/zh/pinterest) [Facebook](https://snapany.com/zh/facebook) [VK](https://snapany.com/zh/vk) [Snapchat](https://snapany.com/zh/snapchat) [Threads](https://snapany.com/zh/threads) [Suno](https://snapany.com/zh/suno) 。

### 其他

- [聚合翻译](https://openl.club/)
- [Scrcpy](https://github.com/Genymobile/scrcpy)
    - 手机投屏电脑
- [Zoho survey](https://www.zoho.com.cn/survey/) 
    - 免费在线问卷
- [chatcrypt](https://client.chatcrypt.com/)
    - 速开匿名聊天室
- [whatismyipaddress](https://whatismyipaddress.com/)

## 软件推荐

- Chrome browser
    - 无需多言
- visual studio code
    - 无需多言
- [everything](https://www.voidtools.com/zh-cn/downloads/)
    - 快速搜寻各种文件样例，支持正则表达式匹配
    - 使用较少安装便携版即可
- [utools](https://u.tools/)（便捷工具箱，下面跟一些好用插件，有空写个个人配置推荐）
    - 网页快开（快速使用喜欢的引擎搜索）
    - 本地搜索（配合 everything 使用更佳）
    - latex 公式编辑&识别（告别手打复杂无比的数学公式）
- [obsidian](https://obsidian.md/)
    - 轻量化 markdown 笔记软件，本地部署，支持多种插件
    - 类似于 vscode，可以极具个性化
    - [Obsidian 插件集市](https://pkmer.cn/products/plugin/pluginMarket/)
- sunshine+moonlight（看第二栏就够了，相信看完远程控制也会了）
    - [屏幕扩展教程](https://blog.csdn.net/weixin_46065314/article/details/136428076)
    - 远程控制教程（ToBeDone）
- [知云文献翻译](https://www.zhiyunwenxian.cn/)
    - 即划即翻

## 软件配置
### chrome 配置（Extensions for chrome）

> 一些自己在用的方便插件，大多来自 chrome store 或者 github，自备魔法，或者自己搜索。

- [沉浸式翻译](https://chromewebstore.google.com/detail/%E6%B2%89%E6%B5%B8%E5%BC%8F%E7%BF%BB%E8%AF%91-%E7%BD%91%E9%A1%B5%E7%BF%BB%E8%AF%91%E6%8F%92%E4%BB%B6-pdf%E7%BF%BB%E8%AF%91-%E5%85%8D%E8%B4%B9/bpoadfkcbjbfhfodiogcnhhhpibjhbnh)
    - 网页翻译，比较好的一点是能够保留原文；默认微软/谷歌翻译，时而网络问题导致错误；可以自己配置 api
- [沙拉查词](https://chromewebstore.google.com/detail/cdonnmffkdaoajfknoeeecmchibpmkmg)
    - 划词翻译
- [广告拦截器 - 1Block](https://chromewebstore.google.com/detail/%E5%B9%BF%E5%91%8A%E6%8B%A6%E6%88%AA%E5%99%A8-1block/jajikjbellknnfcomfjjinfjokihcfoi)
    - 拦截广告
- [GinsMooc](https://github.com/ginnnnnncc/GinsMooc)
- [bilibili哔哩哔哩下载助手](https://chrome.google.com/webstore/detail/bfcbfobhcjbkilcbehlnlchiinokiijp)
    - 在网页端实现缓存功能，**请勿用于违法行为**

### vscode 插件/配置

> 有时候只记得自己用过，但是怎么设置/调了哪些是一点不记得了；对于 python、c++等相关插件都很熟，就不讲了。

- [codesnap](https://blog.csdn.net/qq_51165234/article/details/126201838)

- [verilog](https://blog.csdn.net/SEU_wzx/article/details/126804348)
    - verilog 基本语法纠错/代码高亮
- [background](https://blog.csdn.net/weixin_44112083/article/details/125223060)
    - 让你的 vscode 不那么单调

### Linux 配置

#### zsh
- zsh 安装与使用（教程较多，自行搜索）
- [zsh技巧——devv的回答](https://devv.ai/search?threadId=dri8mmonqh34)
#### conda
- [conda介绍](https://dev.to/bowmanjd/python-tools-for-managing-virtual-environments-3bko#conda)
#### Volatility
- [volatility 配置](https://www.cnblogs.com/Jinx8823/p/16642215.html)

### Obsidian 配置

#### 社区插件

> 我自己使用的一些社区插件。



#### 其他

> [最佳实践](https://coffeetea.top/zh/best-practices/)
> 
> [社区插件](https://coffeetea.top/zh/community-plugins/)

- 字体
    - 中文：[霞鹜字体](https://coffeetea.top/zh/best-practices/obsidian-font-lxgw)
        - 个人感觉挺好看的
    - 英文：用的就是 obsidian 带的 Times New Roman
## Others

- [WayToAGI > 工具](https://waytoagi.feishu.cn/wiki/FVGfwjMtriTDUvkwqvwcYisongh?table=tblp81WDObH3I20H&view=vewM2PB3Iu)
    - [AI工具箱](https://www.amz123.com/ai)
- [A.tool](https://www.a.tools/)
- [tonycrane's toolbox](https://note.tonycrane.cc/cs/tools/toolbox/)
- [Bowling's TechStack](https://note.bowling233.top/%E5%AE%9E%E7%94%A8%E6%8A%80%E8%83%BD/%E5%B0%8F%E5%B7%A5%E5%85%B7/)
- [lddgo](https://www.lddgo.net/)
- [Tboxn](https://www.tboxn.com/)