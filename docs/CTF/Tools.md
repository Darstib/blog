---
tags:
  - notes
comments: true
dg-publish: true
---

> [!SUMMARY]
>
> CTF 学习过程中用到的工具；后来也把一些比较好的文章放在里面了。

## I 综合性网站

- [mzy0](https://ctf.mzy0.com/)
- [随波逐流](http://1o1o.xyz/)

## II 学习平台

- [Hello-ctf](https://hello-ctf.com/)
- [CTF-wiki](https://ctf-wiki.org/)
- [Practical CTF](https://book.jorianwoltjer.com/)

## III 练习&赛事平台

- [ZJUBUS](https://zjusec.com/)
    - 需要 ZJU 校网
- [NSSCTF](https://www.nssctf.cn/problem)
- [BUUCTF](https://buuoj.cn/challenges)
- [bugku](https://ctf.bugku.com/)
- [cryptohack](https://cryptohack.org/challenges/) or [cryptopals](https://cryptopals.com/)
- [Ethernaut 题库闯关题解](https://learnblockchain.cn/column/19)
- [ctftime](https://ctftime.org/ctfs)
    - 国内外知名赛事
- [CTF-writeups-public](https://shiltemann.github.io/CTF-writeups-public/)
## IV Web

- [BurpSuite](https://portswigger.net/burp/releases)
    - [BurpSuite 配置](http://testingpai.com/article/1715763803515)
- [Githack](https://github.com/lijiejie/GitHack)
- [regex101](https://regex101.com/)
    - 可以 debug 看到详细的正则匹配过程，然后利用匹配步数限制来绕过检测
- [DNS lookup](https://www.nslookup.io/)
- [CTF Web信息搜集](https://rickliu.com/posts/24259a52c7ee/index.html)
- [csdn-webshell 工具流量特征分析](https://blog.csdn.net/qq_53577336/article/details/125048353)
## V MISC

- [PuzzleSolver](https://github.com/Byxs20/PuzzleSolver)
    - 现在获取需要一些“代价”
### V.1 图片类

- [Aperi'Solve](https://aperisolve.com)
    - 图片一把梭
- [steghide](https://steghide.sourceforge.net/download.php)
    - [medium——Steghide Tool](https://medium.com/@ece11106.sbit/steghide-tool-ec74edd69de4)
- [Barcode 阅读器](https://demo.dynamsoft.com/barcode-reader/)
    - 很多类型的二维码都能扫
- [fotoforensics](https://fotoforensics.com/)
    - 图像取证分析
- [blind_watermark](https://github.com/guofei9987/blind_watermark)
    - 直接嵌入的盲水印
- [BlindWaterMark](https://github.com/chishaxie/BlindWaterMark)
    - 相似图嵌入的盲水印
- [hex](https://hexed.it/)
    - 在线十六进制编辑器
- [gaps](https://github.com/nemanja-m/gaps)
    - 自动拼图
- [Visual_cryptography](https://www.wikiwand.com/en/articles/Visual_cryptography)
    - 对两张图像进行异或
    - [例题](https://wilige.top/2018/09/26/NTFS%E6%95%B0%E6%8D%AE%E6%B5%81%E9%9A%90%E5%86%99/)
- [Alternate Data Streams (ADS)](https://book.jorianwoltjer.com/windows/alternate-data-streams-ads)
- [Deformed-Image-Restorer](https://github.com/AabyssZG/Deformed-Image-Restorer)
    - 图片宽高自动爆破修复

- [ctf101-misc-slider](https://slides.tonycrane.cc/CTF101-2023-misc/lec2/#/3/5)
    - 也许该好好看看？

### V.2 压缩包

- [APPNOTE-6.3.9.TXT](https://pkware.cachefly.net/webdocs/APPNOTE/APPNOTE-6.3.9.TXT)
    - 4.0 ZIP Files
- [zip 伪加密检测](https://ctfever.uniiem.com/tools/pseudo-encrypted-zip-check)
- [CRC32-Tools](https://github.com/AabyssZG/CRC32-Tools)
- [bkcrack](https://github.com/kimci86/bkcrack)
    - [zip明文攻击](https://www.uf4te.cn/posts/3a71eb8.html)
    - [使用明文攻击破解加密的zip文件](https://www.poboke.com/crack-encrypted-zip-file-with-plaintext-attack.html)
### V.3 音频类

- [audio-decoder-adaptive](https://morsecode.world/international/decoder/audio-decoder-adaptive.html)
    - 直接根据音频自己解莫斯密码
- [slienteye](https://achorein.github.io/silenteye/)
- [audacity](https://www.audacityteam.org/)
- [放屁音乐网](https://www.fangpi.net/)
    - 下载原音乐，请勿侵权商用
- [常见题型](https://blog.csdn.net/qq_51652400/article/details/123504708)

### V.4 OSINT 类

> 什么是 [OSINT](https://www.wikiwand.com/en/articles/Open-source_intelligence) ？

-  [Digital-Privacy](https://github.com/ffffffff0x/Digital-Privacy/blob/master/README.zh-cn.md#manual)
    - 一个巨大的开源信息站点收集项目
- [谷歌地图](https://www.google.com/maps)
- [百度地图](https://map.baidu.com/)
- [高德地图](https://ditu.amap.com/)
- [GeoSpy](https://geospy.ai/)
    - 根据图片使用 AI 寻找地点（当然，不是很准，但是他的描述中可能会有你本来没注意到的地方）
- 太阳角度、阴影长度等太阳相关
    - [suncalc](https://www.suncalc.org/)
    - 时间→位置互相估计
- 飞机航班信息
    - [flightaware](https://flightaware.com)
    - [flightradar24](https://flightradar24.com)
    - [adsbexchange](https://adsbexchange.com)
    - 估计方向，位置，时间等
- 风景信息→Yandex 搜索
- 天气信息、云层信息等

- [web archive](https://web.archive.org/)
    - 网页存档



### V.5 流量分析

- [wireshark](https://www.wireshark.org/#downloadLink)
- [PcapNG File Format](https://pcapng.com/)

![](attachments/Tools.png)

- [pcapng 文件格式](https://blog.csdn.net/m0_53887937/article/details/133978428)
    - [文件提取](https://zgao.top/%E4%BB%8Ewireshark%E6%B5%81%E9%87%8F%E4%B8%AD%E6%8F%90%E5%8F%96%E6%96%87%E4%BB%B6/)
- [pcap fix](https://f00l.de/hacking/pcapfix.php)

### V.6 内存取证

- [LovelyMem](https://github.com/Tokeii0/LovelyMem)
- [csdn-volatility 的安装与使用](https://blog.csdn.net/weixin_44895005/article/details/123917324)
- [ctf101-misc](https://slides.tonycrane.cc/CTF101-2023-misc/lec3/#/2)

### V.7 区块链与以太坊

- [remix](https://remix.ethereum.org/)
    - solidity 在线编辑平台
- [ethernaut](https://ethernaut.openzeppelin.com/)
    - 著名以太坊智能合约入门题目集
    - [Youtube上的讲解](https://www.youtube.com/playlist?list=PLO5VPQH6OWdWh5ehvlkFX-H3gRObKvSL6)
- [powfaucet](https://sepolia-faucet.pk910.de/)
      -  sepolia 中 ETH 的获取源
- [Ethereum Unit Converter](https://eth-converter.com/)
- [鹤翔万里——以太坊区块链合约安全基础](https://www.bilibili.com/video/BV1q2421Z7NK/)
- [chainflag](https://chainflag.org/challenges)

### V.8 PDF

- [Poppler (software)](https://www.wikiwand.com/en/articles/Poppler_(software))

### V.9 其他

- [Italic Text Generator](https://lingojam.com/ItalicTextGenerator)
    - ASCII 绕过
- [文件魔数](https://www.wikiwand.com/en/articles/List_of_file_signatures)
- [键盘按键代码](https://www.lizhanglong.com/Tools/KeyCode)
- [Tupper's self-referential formula](https://www.wikiwand.com/en/articles/Tupper%27s_self-referential_formula)
    - [tuppers-formula](https://tuppers-formula.ovh/)
- [Zero-Width Characters](https://medium.com/@umpox/be-careful-what-you-copy-invisibly-inserting-usernames-into-text-with-zero-width-characters-18b4e6f17b66)
    - [zero-width-web](https://yuanfux.github.io/zero-width-web/)
- [新佛曰](http://hi.pcmoe.net/buddha.html)
- 网络空间搜索
    - [钟馗之眼](https://www.zoomeye.org/)
    - [fofa](https://fofa.info/)
    - [shodan](https://www.shodan.io/)
- [codesearch](https://codesearch.aixcoder.com/#/)
- [sourcegraph](https://sourcegraph.com/search)
- [VirusTotal](https://www.virustotal.com/gui/home/upload)
    - 文档、url 等病毒检测

## VI Crypto

- [CyberChef](https://gchq.github.io/CyberChef/)
    - 赛博厨子
- [cipher identifier](https://www.boxentriq.com/code-breaking/cipher-identifier)
- [ciphey](https://github.com/Ciphey/Ciphey)
    - 自称快于 CyberChef，且捕获类似于 flag{content} 的结果（如果实际的 flag 比较奇怪，可能导致无法解出）
    - 基本使用：
        - `ciphey -t "encode_flag"`
        - `ciphey -f flag.txt`
    - [简单示例](attachments/CTF%20tools.png)
- [quipqiup](https://quipqiup.com/) or  [SubstitutionBreaker](https://gitlab.com/guballa/SubstitutionBreaker)
    - 换位密码
- [factordb](http://factordb.com/)
    - 大数因式分解，支持的数据大小是我所见过最大的
- [codext](https://github.com/dhondta/python-codext)
    - 更全的解码 python 库
- [boxentriq](https://www.boxentriq.com/) <- 支持小范围爆破
    - [caesar-cipher](https://www.boxentriq.com/code-breaking/caesar-cipher)
    - [vigenere-cipher](https://www.boxentriq.com/code-breaking/vigenere-cipher) 
- [sagecell 在线](https://sagecell.sagemath.org/)
    - [sage文档](https://doc.sagemath.org/html/en/tutorial/)
- [UU在线工具](https://uutool.cn/)
    - [文本文件合并](https://uutool.cn/txt-merge/)
- [basecrack](https://github.com/mufeedvh/basecrack/) <- base 系列爆破
    - [base64decode](https://www.base64decode.org/) 还支持文件解码
- [bugku](https://ctf.bugku.com/tools)
- [rsa-wiener-attack](https://github.com/pablocelayes/rsa-wiener-attack) or [RsaCtfTool](https://github.com/RsaCtfTool/RsaCtfTool)
- 不明觉厉系列：
    - [dcode](https://www.dcode.fr/)
    - [dencode](https://dencode.com/)
- [CTF 常见编码及加解密](https://www.cnblogs.com/ruoli-s/p/14206145.html)
## VII 泛工具箱

- [CTFtools-wiki](https://github.com/ProbiusOfficial/CTFtools-wiki)
- [Hello-ctf](https://hello-ctf.com/ToolKit/)
- [ctf-tools](https://github.com/zardus/ctf-tools)
- https://blog.51cto.com/hsqcpp/7939098
- https://github.com/Threekiii/Awesome-CTF
- [ctfever](https://ctfever.uniiem.com/)
- [CTFNOTE](https://github.com/TFNS/CTFNote)
- [Openctf的工具箱](https://ns.openctf.net/learn/misc.html#%E5%B8%B8%E8%A7%81%E9%A2%98%E5%9E%8B%E5%8F%8A%E5%B7%A5%E5%85%B7)

## VIII CTF101

- [Flag提交网站](https://ctf.zjusec.com/games/3/challenges)
- [实验网站](https://courses.zjusec.com/slides/)
- [智云链接](https://classroom.zju.edu.cn/coursedetail?course_id=63047)
- [一个小总结](https://juruo123.github.io/2024/07/02/CTF/)

