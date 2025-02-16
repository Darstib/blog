import os
import re


def process_markdown_content(content):
    """
    处理Markdown文件的内容，确保各个文本块之间有且只有一行空行。
    """
    # 找到前置区块（front_matter）的范围
    separator_index = content.find("---")
    if separator_index != -1:
        second_separator_index = content.find("---", separator_index + 3)
        if second_separator_index != -1:
            front_matter = content[: second_separator_index + 3] + "\n"  # 前置区块
            body = content[second_separator_index + 3 :]  # 正文
        else:
            # 只有一个 `---`，假设没有 front_matter
            front_matter = ""
            body = content
    else:
        front_matter = ""
        body = content

    # 初始化变量
    lines = body.splitlines(keepends=True)
    formatted_lines = []
    in_code_block = False
    in_html_block = False

    def add_block_to_result(block):
        """
        添加一个块到结果中，确保块之间有且只有一行空行。
        """
        if block:
            # 确保块与前后内容有且只有一行空行
            if formatted_lines and formatted_lines[-1].strip() != "":
                formatted_lines.append("\n")
            formatted_lines.extend(block)
            if formatted_lines[-1].strip() != "":
                formatted_lines.append("\n")

    i = 0
    while i < len(lines):
        line = lines[i]

        # 处理代码块
        if line.startswith("```"):
            code_block = []
            code_block.append(line)
            in_code_block = not in_code_block
            i += 1
            while i < len(lines):
                line = lines[i]
                code_block.append(line)
                if line.startswith("```"):
                    in_code_block = not in_code_block
                    break
                i += 1
            add_block_to_result(code_block)
            i += 1
            continue

        # 处理HTML标签块
        if re.match(r"^\s*<\w+", line) and not in_code_block:
            html_block = []
            while i < len(lines) and not re.match(r"^\s*</\w+>", lines[i]):
                html_block.append(lines[i])
                i += 1
            if i < len(lines):
                html_block.append(lines[i])  # 加上结束标签
            add_block_to_result(html_block)
            i += 1
            continue

        # 处理表格块
        if re.match(r"^\|.*\|$", line):
            table_block = []
            while i < len(lines) and re.match(r"^\|.*\|$", lines[i]):
                table_block.append(lines[i])
                i += 1
            add_block_to_result(table_block)
            continue

        # 处理注释块
        if line.startswith(">"):
            comment_block = []
            while i < len(lines) and lines[i].startswith(">"):
                comment_block.append(lines[i])
                i += 1
            add_block_to_result(comment_block)
            continue

        # 处理列表块
        if line.lstrip().startswith("-") or re.match(r"^\d+\.\s", line):
            list_block = []
            while i < len(lines) and (
                lines[i].lstrip().startswith("-") or re.match(r"^\d+\.\s", lines[i])
            ):
                list_block.append(lines[i])
                i += 1
            add_block_to_result(list_block)
            continue

        # 处理脚注缩进块
        if re.match(r"^\[\^\w+\]:", line):
            indent_block = []
            indent_block.append(line)
            i += 1
            while i < len(lines):
                # 检查当前行是否是缩进行，若是则继续将其添加到缩进块
                if lines[i].startswith("    ") or lines[i].startswith("\t"):
                    indent_block.append(lines[i])
                    i += 1
                else:
                    break
            add_block_to_result(indent_block)
            continue

        # 处理 more 注释行
        if "<!-- more -->" in line:
            formatted_lines.append(line)
            if formatted_lines[-1].strip() != "":
                formatted_lines.append("\n")
            i += 1
            continue

        # 处理数学公式块
        if line.startswith("$$"):
            math_block = []
            math_block.append(line)
            i += 1
            # 读取公式块中的内容，直到找到结束符号"$$"
            while i < len(lines):
                current_line = lines[i]
                math_block.append(current_line)
                if current_line.startswith("$$") and len(math_block) > 1:
                    break
                i += 1
            # 移除公式块内部的多余空行
            trimmed_math_block = [
                line for line in math_block if line.strip() or line.startswith("$$")
            ]
            add_block_to_result(trimmed_math_block)
            i += 1
            continue

        # 处理普通行
        if line.strip() == "":
            # 空行，继续处理
            i += 1
            continue

        # 普通文本行
        formatted_lines.append(line)
        if formatted_lines[-1].strip() != "":
            formatted_lines.append("\n")
        i += 1

    # 组合最终内容
    # 确保 front_matter 和正文之间有一个空行
    if front_matter:
        formatted_front_matter = front_matter + "\n"
    else:
        formatted_front_matter = ""

    return formatted_front_matter + "".join(formatted_lines)


def add_extra_newlines_to_markdown(folder_path):
    """
    遍历目标文件夹及其子文件夹，处理Markdown文件，确保内容块之间有且只有一行空行。
    """
    for root, _, files in os.walk(folder_path):
        for filename in files:
            if filename.endswith(".md"):
                file_path = os.path.join(root, filename)
                with open(file_path, "r", encoding="utf-8") as file:
                    content = file.read()

                # 处理Markdown内容
                modified_content = process_markdown_content(content)

                # 写回文件
                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(modified_content)

                print(f"Processed: {file_path}")


# 使用示例
folder_path = "/mnt/d/a_ob/vaults/public_note/notes/CS-I"  # 替换为你目标文件夹的路径
add_extra_newlines_to_markdown(folder_path)
