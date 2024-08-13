# import os


# def rename_files_in_directory(directory):
#     # 遍历目录及其子目录
#     for root, dirs, files in os.walk(directory):
#         for file in files:
#             # 检查文件名中是否有空格
#             if " " in file:
#                 # 替换空格为短横线
#                 new_file_name = file.replace(" ", "-")
#                 # 构建完整的旧文件路径和新文件路径
#                 old_file_path = os.path.join(root, file)
#                 new_file_path = os.path.join(root, new_file_name)

#                 # 重命名文件
#                 os.rename(old_file_path, new_file_path)
#                 print(f'Renamed: "{old_file_path}" to "{new_file_path}"')


# if __name__ == "__main__":
#     # 指定要处理的目录路径
#     directory_path = "/mnt/d/a_ob/vaults/public_note/"
#     rename_files_in_directory(directory_path)

import os
import re


def replace_spaces_in_markdown(directory):
    # 遍历目录及其子目录
    for root, dirs, files in os.walk(directory):
        for file in files:
            # 只处理 Markdown 文件
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                try:
                    # 读取文件内容
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()

                    # 替换被()包裹的所有%20为-
                    new_content = re.sub(
                        r"\(([^()]*?)%20([^()]*?)\)",
                        lambda m: f"({m.group(1)}-{m.group(2)})",
                        content,
                    )
                    new_content = re.sub(
                        r"\((.*?)\)",
                        lambda m: m.group(0).replace("%20", "-"),
                        new_content,
                    )

                    # 如果内容有变化，则写回文件
                    if content != new_content:
                        with open(file_path, "w", encoding="utf-8") as f:
                            f.write(new_content)
                        print(f'Updated: "{file_path}"')
                except Exception as e:
                    print(f'Error processing file "{file_path}": {e}')


if __name__ == "__main__":
    # 指定要处理的目录路径
    directory_path = "/mnt/d/a_ob/vaults/public_note"
    replace_spaces_in_markdown(directory_path)
