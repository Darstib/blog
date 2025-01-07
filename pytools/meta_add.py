import os

# 目标文件夹路径
path = "/mnt/d/a_ob/docs/notes"  # 替换为你的文件夹路径

# 旧结构和新结构
old_header_structure = """---
tags:
  - notes
---
"""

new_header_structure = """---
tags:
- notes
---
"""


def replace_header_in_file(file_path):
    with open(file_path, "r+", encoding="utf-8") as file:
        content = file.readlines()

        # 检查文件开头是否包含旧结构
        if (
            len(content) >= 5
            and "".join(content[:5]).strip() == old_header_structure.strip()
        ):
            # 替换为新结构
            content[:5] = new_header_structure.splitlines(keepends=True)

            # 重写文件内容
            file.seek(0)
            file.writelines(content)
            file.truncate()
            print(f"Replaced header in: {file_path}")
        else:
            print(f"No matching header found in: {file_path}")


def replace_header_in_markdown_files(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if filename.endswith(".md"):
                file_path = os.path.join(root, filename)
                replace_header_in_file(file_path)


# 执行替换操作
replace_header_in_markdown_files(path)
