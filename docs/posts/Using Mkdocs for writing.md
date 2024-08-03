---
date: 2024-06-29
tags:
  - blog
  - 杂记
---
***

在使用 Mkdocs 作博客笔记时，发现其他人的文章有一些比较有意思的格式，美观方便，故学习参考，此处主要记录用法备忘，具体配置请转移至[官方文档](https://squidfunk.github.io/mkdocs-material/reference/) 进行查看，我只会给出基本的配置教程；大多数格式都是可以嵌套使用的，文中不会过多提及，请自行探索。

> TonyCrane 学长写了一份详尽的[降压宝典](https://hypotensor.tonycrane.cc/ta/) ，旨在完善细节以便呈现更好地效果，有兴趣可以看看。

<!-- more -->

## Admonitions

主要用于添加大段资料批注

### madocs.yml 配置

??? note "mkdocs.yml 配置"
  ```yml
    theme:
      icon:
        admonition:
          note: octicons/tag-16
          abstract: octicons/checklist-16
          info: octicons/info-16
          tip: octicons/squirrel-16
          success: octicons/check-16
          question: octicons/question-16
          warning: octicons/alert-16
          failure: octicons/x-circle-16
          danger: octicons/zap-16
          bug: octicons/bug-16
          example: octicons/beaker-16
          quote: octicons/quote-16
  ```

### 用法

#### 注释块

我们可以使用 **!!!** + 类型 + "标题" 标明告诫块，在其下使用缩进表明其内容所在

> 可以使用空表示不需要标题

例如
```note
!!! note "这是一个注释块"

    这里是内容
```

那么呈现效果如下：

!!! note "这是一个注释块"

    这里是内容

#### 可折叠注释块

将三个 **!** 换为三个 **?** 即可，如果想要呈现展开的状态，再加一个 **+** 号即可

???+ tip "这是可折叠注释块"

    这里是tips

#### 内联块

在类型后加上 **inline** 可构成内联块放在左侧，再加上 **end** 可放在右侧（个人偏爱）

```notes
!!! info inline end "Lorem ipsum"

    Lorem ipsum dolor sit amet, consectetur
    adipiscing elit. Nulla et euismod nulla.
    Curabitur feugiat, tortor non consequat
    finibus, justo purus auctor massa, nec
    semper lorem quam in massa.
```
效果如下

!!! info inline end "这是内联块"

    这里是文本
这里是文本这里是文本这里是文本这里是文本这里是文本这里是文本
这里是文本这里是文本这里是文本这里是文本这里是文本这里是文本
这里是文本这里是文本这里是文本这里是文本这里是文本这里是文本
这里是文本这里是文本这里是文本这里是文本这里是文本这里是文本
这里是文本这里是文本这里是文本这里是文本这里是文本这里是文本
这里是文本这里是文本这里是文本这里是文本这里是文本这里是文本
这里是文本这里是文本这里是文本这里是文本这里是文本这里是文本

## Annotations

### mkdocs.yml 配置

??? note "mkdocs.yml 配置"

    ```yml
    markdown_extensions:
      - attr_list
      - md_in_html
      - pymdownx.superfences
    theme:
      icon:
        annotation: material/plus-circle
    ```

### 用法

下面是一段示例格式：

```note

    这里是文本这里是文本这里是(1)文本这里是文本这里是文本这里是文本。
    { .annotate } # 记得换行

    1.  : 这是一段旁注
```

效果如下

这里是文本这里是文本这里是(1)文本这里是文本这里是文本这里是文本。
{ .annotate }

1.  : 这是一段旁注

注意`{ .annotate }` 声明&一行空格

这个可以在大多场合使用，如标题，表格甚至嵌套使用，但是考虑到基本不会用，不加讨论

## Buttons

### mkdocs.yml 配置

??? note "mkdocs.yml 配置"

    ```yml
    markdown_extensions:
        - attr_list
    ```

### 用法

```note
[click here for more](#){ .md-button }
// 即使用 `{ .md-button}` 进行声明， `#` 中可填写链接，默认是该页面的一级标题
[click here for more](#){ .md-button .md-button--primary }
// 加上 `.md-button--primary` 表示填充
```

[click here for more](#){ .md-button }

[click here for more](#){ .md-button .md-button--primary }

## Code blocks

### mkdocs.yml 配置

??? note "mkdocs.yml 配置"

    ```yml
    markdown_extensions:
      - pymdownx.highlight:
          anchor_linenums: true
          line_spans: __span
          pygments_lang_class: true
      - pymdownx.inlinehilite
      - pymdownx.snippets
      - pymdownx.superfences
    theme:
      features:
        - content.code.copy
    ```

### 用法

使用三对反引号 **`** 将代码包裹即可，注意：代码适当缩进

其他操作：

- 可在前三个反引号后添加代码语言以便高亮
- 还可添加属性 **title="标题"** 来取标题
- 还可添加注释，要求使用对应代码语言的注释方法，如python就是 **# (1)**，不想要显示 **#** 的话在 **(1)** 后面添加 **!** 即可
- 添加行号 **linenums="<start>"** start 表示起始行号
- 高亮某行 **hl_lines="行号"** 行号可用空格间隔高亮多行，可用 **a-b** 表示高亮行数范围
- 使用 **#!python** 使得内联代码块可以高亮，例如 `#!python print(i)`

```py linenums="1" title="first.py" hl_lines="2"

print("hello world!") # (1)!
for i in range(1, 10):
    print(i)
```

1. 打印“hello world”

## Content tabs

### mkdocs.yml 配置

??? note "mkdocs.yml 配置"

    ```yml
    - pymdownx.tabbed:
      alternate_style: true
      slugify: !!python/object/apply:pymdownx.slugs.slugify
          kwds:
          case: lower
    ```

### 用法

使用 **===** 后使用英文双引号包裹 **table_name** ，之后空一行加上内容，如：

```c
=== "C"

    ``` c
    #include <stdio.h>

    int main(void) {
      printf("Hello world!\n");
      return 0;
    }
    ```

=== "C++"

    ``` c++
    #include <iostream>

    int main(void) {
      std::cout << "Hello world!" << std::endl;
      return 0;
    }
    ```
```

效果如下：

=== "C"

    ``` c
    #include <stdio.h>

    int main(void) {
      printf("Hello world!\n");
      return 0;
    }
    ```
=== "C++"

    ``` c++
    #include <iostream>

    int main(void) {
      std::cout << "Hello world!" << std::endl;
      return 0;
    }
    ```

## Data tables

### mkdocs.yml 配置

??? note "mkdocs.yml 配置"

    ```yml
    markdown_extensions:
        - tables
    ```

### 用法

（与 markdown 中是一致的）

| Method      | Description                          |
| :---------: | :----------------------------------: |
| `GET`       | :material-check:     Fetch resource  |
| `PUT`       | :material-check-all: Update resource |
| `DELETE`    | :material-close:     Delete resource |

> 关于一些表情请看 **Icons, Emojis**

## Diagrams

### mkdocs.yml 配置

??? note "mkdocs.yml 配置"

    ```yml
    markdown_extensions:
      - pymdownx.superfences:
          custom_fences:
            - name: mermaid
              class: mermaid
              format: !!python/name:pymdownx.superfences.fence_code_format
    ```

### 用法

下面我们看看 flowcharts 的表现形式，其他不加解释
因为我的笔记主要使用 obsidian 制作流程图

```
    ``` mermaid
    graph LR
      A[Start] --> B{Error?};
      B -->|Yes| C[Hmm...];
      C --> D[Debug];
      D --> B;
      B ---->|No| E[Yay!It works!];
    ```
```

下面是效果，可以看出不同的括号的呈现效果不同

``` mermaid
graph LR
  A[Start] --> B{Error?};
  B -->|Yes| C[Hmm...];
  C --> D[Debug];
  D --> B;
  B ---->|No| E[Yay! It works!];
```

## Footnotes

### mkdocs.yml 配置

??? note "mkdocs.yml 配置"

    ```yml
    markdown_extensions:
      - footnotes
    theme:
      features:
        - content.footnote.tooltips
    ```

### 用法

其实使用方法与 Markdown 的语法是 ^^基本^^ 一致的（鼠标悬停可查看）

```
    Lorem ipsum[^1] dolor sit amet, consectetur adipiscing elit.[^2]

  Lorem ipsum[^1] dolor sit amet, consectetur adipiscing elit.[^2]
  [^1]: Lorem ipsum dolor sit amet, consectetur adipiscing elit.
  [^2]:
      Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor massa, nec semper lorem quam in massa.
```

Lorem ipsum[^1] dolor sit amet, consectetur adipiscing elit.[^2]
[^1]: Lorem ipsum dolor sit amet, consectetur adipiscing elit.
[^2]:
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor massa, nec semper lorem quam in massa.

## Grids

### mkdocs.yml 配置

??? note "mkdocs.yml 配置"

    ```yml
        markdown_extensions: 
          - attr_list
          - md_in_html
    ```

<div class="grid card" markdown>

=== "Unordered list"

    * Sed sagittis eleifend rutrum
    * Donec vitae suscipit est
    * Nulla tempor lobortis orci

=== "Ordered list"

    1. Sed sagittis eleifend rutrum
    2. Donec vitae suscipit est
    3. Nulla tempor lobortis orci

``` title="Content tabs"
=== "Unordered list"

    * Sed sagittis eleifend rutrum
    * Donec vitae suscipit est
    * Nulla tempor lobortis orci

=== "Ordered list"

    1. Sed sagittis eleifend rutrum
    2. Donec vitae suscipit est
    3. Nulla tempor lobortis orci
```

</div>



## Icons, Emojis

### mkdocs.yml 配置

??? note "mkdocs.yml 配置"
    ```yml
    markdown_extensions:
      - attr_list
      - pymdownx.emoji:
          emoji_index: !!python/name:material.extensions.emoji.twemoji
          emoji_generator: !!python/name:material.extensions.emoji.to_svg
    ``` 

### 用法

表情符号可以通过将表情符号的短代码放在两个冒号之间来集成到 Markdown 中

我们可以在[官方文档上](https://squidfunk.github.io/mkdocs-material/reference/icons-emojis/#usage:~:text=%E5%AE%9A%E4%B9%89%E5%9B%BE%E6%A0%87%E3%80%82-,search) 进行搜索，也可以去 [Emojipedia](https://emojipedia.org/) 上复制过来😀
