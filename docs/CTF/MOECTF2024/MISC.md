---
tags:
  - notes
comments: true
dg-publish: true
level: ctfwp
---

> python jail 部分单独放在 MISC/pyjial.md 中。

### 拼图羔手

图片变为 4x4 ，简单的 python 代码就不能够帮助我们拼图了，但是有一个比较好的工具 [gaps](https://github.com/nemanja-m/gaps)，我们把图片拼为一张图 tmp.png 后，运行：

```shell
gaps run tmp.png solution.png --generations=20 --population=600 --size=122
```

即可拿到[二维码](attachments/solution.png)，扫码得到：

`balabalbalablbalblablbalabala//nihaopintugaoshou//encoded_flag{71517ysd%ryxsc!usv@ucy*wqosy*qxl&sxl*sbys^wb$syqwp$ysyw!qpw@hs}`

根据 encode.py 和 StrangeCharacterHint ，做出了如下解码脚本：

```python title="decode.py"
# https://ctf.xidian.edu.cn/games/10/challenges?challenge=123

def self_decode(encoded_text):
    code_setting_first = "doanythigfruebcjklmqpswvxz"
    code_setting_sec = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number_setting = "0123456789"
    decoded_text = ""

    for char in encoded_text:  # 处理非数字部分
        if char in code_setting_first:
            if 116 <= ord(char) <= 122:
                decoded_text += chr(ord(char) - 19)
            elif 97 <= ord(char) <= 103:
                decoded_text += chr(ord(char) + 19)
            elif 104 <= ord(char) <= 115:
                decoded_text += chr(219 - ord(char))
        elif char in code_setting_sec:
            if 72 <= ord(char) <= 78:
                decoded_text += chr(ord(char) - 7)
            elif 65 <= ord(char) <= 71:
                decoded_text += chr(ord(char) + 7)
            elif 88 <= ord(char) <= 90:
                decoded_text += chr(ord(char) - 9)
            elif 79 <= ord(char) <= 81:
                decoded_text += chr(ord(char) + 9)
            elif 81 <= ord(char) <= 86:
                decoded_text += chr(168 - ord(char))
        elif char not in number_setting:
            decoded_text += char

    import re

    # 处理数字部分
    # 使用正则匹配encoded_text中的第一个数字，并获取其之后的所有数字写入 numbers 字符串中，没有数字则返回原文本
    numbers = re.findall(r"\d+", encoded_text)
    if numbers:
        numbers = numbers[0]
    else:
        return decoded_text
    # print(numbers)
    reversed_numbers = numbers[::-1]
    reversed_decode_numbers = last = numbers[0]
    for i in range(1, len(reversed_numbers)):
        last = str(int(numbers[i]) ^ int(last))
        reversed_decode_numbers += last
    decoded_text += reversed_decode_numbers[::-1]

    return decoded_text


# 使用函数
reversed_encode_flag = "71517ysd%ryxsc!usv@ucy*wqosy*qxl&sxl*sbys^wb$syqwp$ysyw!qpw@hs"[
    ::-1
]

# key = "xixsdxnlUmXixunbGsardftaUixavtitsJxzmtiaU"
# reverse_key = "xixsdxnlUmXixunbGsardftaUixavtitsJxzmtiaU"[::-1]
# decoded_key = self_decode(reverse_key)
# print(decoded_key) "StrangeCharacterStaywithNumberOnSomewhere"

decoded_flag = self_decode(reversed_encode_flag)
print("moectf{" + decoded_flag + "}")
# moectf{hs@dkj!dfhf$kdjfh$ud^hfuh*oeh&oej*fhljd*fvb@chb!vhefi%whf52367}
alphabet = ""
strange_character = ""
nums = ""
for char in decoded_flag:
    if char in "doanythigfruebcjklmqpswvxz":
        alphabet += char
    elif char in "0123456789":
        nums += char
    else:
        strange_character += char

print("moectf{" + alphabet + strange_character + nums + "}")
print("moectf{" + alphabet + nums + strange_character + "}")
# moectf{hsdkjdfhfkdjfhudhfuhoehoejfhljdfvbchbvhefiwhf@!$$^*&**@!%52367}
# moectf{hsdkjdfhfkdjfhudhfuhoehoejfhljdfvbchbvhefiwhf52367@!$$^*&**@!%}

```

但是，这三个结果都是错误的。通过“锤子”尝试获取帮助，管理员给我的提示是：“StrangeCharacterStaywithNumberOnSomewhere 这里的数字不是flag里面出现的数字如果你买这题hint了你会知道这里数字和字母是互相置换的但这个对应的数字需要你去找故而这个hint就是数字和字母的对应关系的展示” 

> 购买 hint: “strange character不能现身flag，对应的数字总是作为他的替身现身flag” 。

尝试了 ascii 码，显然失败了。

最后在交流中，想到键盘上的按键（F1、F2 等按键下面那一行）的映射，过关。

> [!FLAG]
>
> moectf{hs2dkj1dfhf4kdjfh4ud6hfuh8oeh7oej8fhljd8fvb2chb1vhefi5whf52367}

### 每人至少300份

解压缩包，获得 9 个拼图和一个 encode.txt 以及 encode0.py 。

```python title="img_puzzle.py"
from PIL import Image
import numpy as np
import os


def get_edge(image, edge):
    if edge == "left":
        return np.array(image)[:, 0]
    elif edge == "right":
        return np.array(image)[:, -1]
    elif edge == "top":
        return np.array(image)[0, :]
    elif edge == "bottom":
        return np.array(image)[-1, :]


def edge_difference(edge1, edge2):
    return np.sum(np.abs(edge1 - edge2))


def find_best_match(target_edge, images, edge_type):
    best_match = None
    best_score = float("inf")
    for img in images:
        score = edge_difference(target_edge, get_edge(img, edge_type))
        if score < best_score:
            best_score = score
            best_match = img
    return best_match, best_score


def reconstruct_qr(input_folder, output_file):
    image_files = [
        f for f in os.listdir(input_folder) if f.endswith(".png") or f.endswith(".jpg")
    ]
    images = [
        Image.open(os.path.join(input_folder, f)).convert("RGB") for f in image_files
    ]

    tile_width, tile_height = images[0].size
    result_image = Image.new("RGB", (tile_width * 3, tile_height * 3))

    # Find top-left corner (usually contains a positioning square)
    top_left = max(images, key=lambda img: np.sum(np.array(img)[:10, :10] == 0))
    result_image.paste(top_left, (0, 0))
    images.remove(top_left)

    # Complete first row
    for i in range(1, 3):
        target_edge = get_edge(
            result_image.crop((tile_width * (i - 1), 0, tile_width * i, tile_height)),
            "right",
        )
        best_match, _ = find_best_match(target_edge, images, "left")
        result_image.paste(best_match, (tile_width * i, 0))
        images.remove(best_match)

    # Complete first column
    for i in range(1, 3):
        target_edge = get_edge(
            result_image.crop((0, tile_height * (i - 1), tile_width, tile_height * i)),
            "bottom",
        )
        best_match, _ = find_best_match(target_edge, images, "top")
        result_image.paste(best_match, (0, tile_height * i))
        images.remove(best_match)

    # Complete remaining tiles
    for row in range(1, 3):
        for col in range(1, 3):
            left_edge = get_edge(
                result_image.crop(
                    (
                        tile_width * (col - 1),
                        tile_height * row,
                        tile_width * col,
                        tile_height * (row + 1),
                    )
                ),
                "right",
            )
            top_edge = get_edge(
                result_image.crop(
                    (
                        tile_width * col,
                        tile_height * (row - 1),
                        tile_width * (col + 1),
                        tile_height * row,
                    )
                ),
                "bottom",
            )

            best_match = None
            best_score = float("inf")
            for img in images:
                score = edge_difference(
                    left_edge, get_edge(img, "left")
                ) + edge_difference(top_edge, get_edge(img, "top"))
                if score < best_score:
                    best_score = score
                    best_match = img

            result_image.paste(best_match, (tile_width * col, tile_height * row))
            images.remove(best_match)

    result_image.save(output_file)
    print(f"Reconstructed QR code saved as {output_file}")


# 使用函数
input_folder = "imgs/"
output_file = "reconstructed_qr.png"
reconstruct_qr(input_folder, output_file)
```

对于拼图，用上面的简单脚本[获取](attachments/reconstructed_qr.png)，扫码得；

`balabalballablblablbalablbalballbase58lblblblblllblblblblbalblbdjshjshduieyrfdrpieuufghdjhgfjhdsgfsjhdgfhjdsghjgfdshjgfhjdgfhgdh///key{3FgQG9ZFteHzw7W42}??`

可以看到其中有一个 "base58" ，将 `3FgQG9ZFteHzw7W42` 用 base58 解码后尝试提交，通过了……

> [!FLAG]
>
> moectf{we1rd_qrc0d3}

### 解不完的压缩包

在 ctf101 中 ruru 与之类似，当时还有伪加密，这里没有；使用 python 脚本递归解压缩即可；最后获得一个 cccccccrc.zip ，考虑到其中有四个等大的小文本，同时压缩包名字也是提示，学习到这是 crc 碰撞，使用 [CRC32-Tools](https://github.com/AabyssZG/CRC32-Tools) 解开即可，获取密码：`*m:#P7j0` ，解开压缩包获得：

> [!FLAG]
>
> moectf{af9c688e-e0b9-4900-879c-672b44c550ea}

### 时光穿梭机

- [评《维多利亚时代的中国图像》](https://www.chinesefolklore.org.cn/forum/viewthread.php?action=printable&tid=18991) or [评《维多利亚时代的中国图像》：以图证史的他山之石](http://www.99ys.com/home/1970/01/01/08/84714.html)
- [高德地图——王建墓](https://ditu.amap.com/place/B001C8X8E1)

但是医院没找到……

### Find It

图中给出了很多大公司名称：雄峰集团、桔子水晶酒店，定位到小区：“旭景崇盛园”；找到幼儿园：“吉的堡旭景崇盛幼儿园” “吉的堡英佳幼儿园”

> [!FLAG]
>
> moectf{ji_di_bao_you_er_yuan}

### the_secret_of_snowball

JPG 图像损害，修改开头的模数即可 => `Welc0me_t0_the_sec`

继续查看，末尾有 base64，解码 => `ret_life_0f_Misc!`

> [!FLAG]
>
> moectf{Welc0me_t0_the_secret_life_0f_Misc!}

### 捂住一只耳

音频 1 分钟后出现信息：`ok ?63 31 43 31 41 52 31 51 71 101` ascii ？没猜出来。

### ctfer2077

#### 1

二维码扫了，当然是被骗了；继续看，用 zsteg 提取出：`where is the flag ? OK I give you some hints:incomplete LSB` =>  `b1,r,lsb,xy .. text:** "flag is moectf{84d7f247-3cba-4077-ba25-079f3ac7bb8a}"`

> [!FLAG]
>
> moectf{84d7f247-3cba-4077-ba25-079f3ac7bb8a}

### ez_F5

根据题目名称和其中的 copyright 可以知道是 [F5 加密](https://github.com/matthewgao/F5-steganography) (注意图片属性获取密码；使用 java 8)。

> [!FLAG]
>
> moectf{F5_15_s0_lntere5t1n9}

### 罗小黑战记

实话说第一次做 gif 题，但是看完一遍很显然某几帧有东西，[提取出来看看就好](attachments/README.png)，扫二维码。

> [!FLAG]
>
> moectf{y0uu6r3th3m0st3r1nth1sf13ld}

### 杂项入门指北

拿到图片确实是习惯于瞄一眼，然后去看隐写。看了半天，没东西。突然一堆实线中有一段虚线，按照字母将[图片旋转](attachments/README-1.png) => `.... ....- ...- . ..--.- .- ..--.- --. ----- ----- -.. ..--.- - .---- -- .`

> [!FLAG]
>
> moectf{H4VE_A_G00D_T1ME}

### ez_Forensics

> 考察内存取证，先[复习一下](https://slides.tonycrane.cc/CTF101-2023-misc/lec3/#/2)

查看[命令行信息](attachments/WRITEUP.png)，得到 flag：

> [!FLAG]
>
> moectf{WWBGY-TLVC5-XKYBZ}

### Abnormal flag

audacity [查看频谱图](attachments/WRITEUP-1.png)

> [!FLAG]
>
> moectf{09e3f7f8-c970-4c71-92b0-6f03a677421a}

