## 锅里捞面

致敬传奇电报员：

```
.- -.-- -- -.-. .. -.- --.- -..- .... .-. ...-- ..--- ----- . --... -.-. .... .-- ...- -.-- ---.. ....- --.. --. -- ----. ..... ....- ..- --. ----- -.... .---- .... ----. --.- ...- ----. ...-- -.... ----- - .--- - .--- .--- ...-- --... .... ----. .- -... .-.. ....- ..--- .- -... .--- .... ..... -... -...
```

莫斯解码为 `AYMCIKQXHR320E7CHWVY84ZGM954UG061H9QV9360TJTJJ37H9ABL42ABJH5BB`

然后呢？不会了，待看……

## Bytes

16 进制 => 转 bytes 即 8 位二进制 => 尝试拼各种规格的矩形

```python title="bytes_solver.py"
tmp = [0x0, 0x0, ...] # bytes.txt 中的内容

flag_bin = ""
for t in tmp:
    t_bin = bin(t)[2:].zfill(8)
    flag_bin += t_bin

# print(len(flag_bin)) # 6072 = 2^3 * 3 * 11 * 23
factors = [2, 2, 2, 3, 11, 23]
from itertools import chain, combinations


def powerset(iterable):
    """生成可迭代对象的所有子集"""
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


xs = set()
for subset in powerset(factors):
    product = 1
    for num in subset:
        product *= num
    xs.add(product)
xs = list(xs)
xs.sort()

# print(xs)

flag = ""
# for x in xs:
for x in [276]: # 根据结果知道是 276
    for i in range(len(flag_bin)):
        if i % x == 0:
            flag += "\n"
        flag += flag_bin[i]

with open("flag.txt", "w") as f:
    f.write(flag)
```

![](attachments/MISC-2.png)

> [!FLAG]
>
> ZJUCTF{COU_GOU_LIANG_HANG_BA}
## Chess Encoding

依照《名侦探柯南》提示，我们将图片都顺时针旋转 90°，由下至上读取数字，均减一后为 8 进制数；之后 8->2->16 -> ASCII 码，

```python title="chess.py"
chess = [
    "37556236",
    "31763217",
    "47758624",
    "42365648",
    "42158664",
    "42385648",
    "33368663",
    "46382635",
    "38741628",
    "46573648",
    "44353572",
    "26771627",
    "26773622",
    "38756571",
    "34551267",
    "38775268",
    "45153648",
    "36368635",
    "34741286",
]

chess = "".join(chess)

chess_bin = ""
# 对应字符减一后变为 8进制数 转变为 3 位二进制，并合并
for c in chess:
    chess_bin += bin(int(c, 16) - 1)[2:].zfill(3)

# 二进制转换为字符
flag = ""
for i in range(0, len(chess_bin), 8):
    # print(i, int(chess_bin[i : i + 8], 2), chr(int(chess_bin[i : i + 8], 2)))
    flag += chr(int(chess_bin[i : i + 8], 2))

print(flag)
```

> [!FLAG]
>
> ZJUCTF{OKeY_dOkey_I_jusT_1Ove_mE17aN7eI_K0N@n_hopE_U_TO0}

## Master of C++

> [MasterC++ Chatgpt](https://chatgpt.com/share/670e853f-dcf0-8007-8bd4-1e7a4d97853b)

**编译后的 `main` 函数必须只包含一条操作 `eax` 寄存器的指令和一条 `ret` 指令**。这意味着我们不能在运行时进行任何计算，所有的判断必须在编译时完成，使用模板元完成。

```c++
template<int N>
struct prime {
    static const bool value = (N > 1) && (N == 2 || N % 2 != 0) &&
        (N < 9 || (N % 3 != 0 && N % 5 != 0 && N % 7 != 0));
};

int main() {
    return prime<ARG>::value ? 0 : 1;
}
```

![](attachments/MISC-1.png)

> [!FLAG]
>
> ZJUCTF{pR3m4tuR3_0PT1miz4t1oN_1s_thE_R00t_of_4LL_3v1l}

## 小 A 口算

时间充足，python 交互就好:

```python title="alrithmetic"
from pwn import *

context.log_level = "debug"
conn = remote("127.0.0.1", 52428)


# Function to compare two numbers and return the appropriate symbol
def compare_numbers(a, b):
    if a > b:
        return ">"
    elif a < b:
        return "<"
    else:
        return "="


# Receive initial game introduction
intro = conn.recvuntil("Input your choice:")
# print(intro.decode())

# Send '1' as our choice for "Primary school Bachelor"
conn.sendline(b"1")

# Main loop
while True:
    try:
        # Receive a chunk of data with a timeout
        chunk = conn.recvuntil("input '>', '<' or '=' :", timeout=5).decode()
    except EOFError:
        print("Connection closed by remote host")
        break
    except TimeoutError:
        print("Timeout while waiting for prompt. Receiving remaining data...")
        chunk = conn.recv().decode()

    # Find the question in the chunk
    lines = chunk.split("\n")
    question = next((line for line in lines if "?" in line), None)

    if not question:
        print("No more questions. Remaining data:")
        print(chunk)
        break

    # print(f"Question: {question}")

    # Parse the numbers from the question
    numbers = question.split("?")
    a = int(numbers[0].strip())
    b = int(numbers[1].strip())

    # Compare the numbers and send the result
    result = compare_numbers(a, b)
    # print(f"Sending: {result}")
    conn.sendline(result.encode())

# Close the connection
conn.close()
```

![](attachments/MISC.png)

> [!FLAG]
>
> ZJUCTF{WoW_K1n6_0F_5h0-g4Ku-s31_4r1thm3t1c}
