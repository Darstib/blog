import os
import re

# 目标文件夹路径
path = "/mnt/d/a_ob/test/"  # 替换目标文件夹路径
tag_to_remove = "test"  # 要删除的标签

# 正则表达式用于匹配 tags 部分
tags_pattern = re.compile(r"(tags:\s*\n(?:\s*- .*\n)*)", re.DOTALL)


def remove_tag_from_file(file_path):
    with open(file_path, "r+", encoding="utf-8") as file:
        content = file.read()

        # 查找tags部分
        match = tags_pattern.search(content)
        if match:
            tags_section = match.group(0)
            # 删除指定的标签行
            updated_tags_section = re.sub(
                r"^\s*- " + re.escape(tag_to_remove) + r"\s*\n?",
                "",
                tags_section,
                flags=re.MULTILINE,
            )

            # 处理多余的换行符，确保只删除目标标签行后的换行
            updated_tags_section = (
                updated_tags_section.strip() + "\n"
                if updated_tags_section.strip()
                else ""
            )

            # 更新内容
            updated_content = content.replace(tags_section, updated_tags_section)

            # 只在tags部分有变化时重写文件内容
            if updated_content != content:
                file.seek(0)
                file.write(updated_content)
                file.truncate()
                print(f"Removed tag '{tag_to_remove}' in: {file_path}")
            else:
                print(f"Tag '{tag_to_remove}' does not exist in: {file_path}")
        else:
            print(f"No tags section found in: {file_path}")


def remove_tag_from_markdown_files(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if filename.endswith(".md"):
                file_path = os.path.join(root, filename)
                remove_tag_from_file(file_path)


# 执行删除操作
remove_tag_from_markdown_files(path)
