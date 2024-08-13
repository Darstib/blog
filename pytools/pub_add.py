import os

# 目标文件夹路径
path = "/mnt/d/a_ob/public_note/notes"  # 替换为文件夹路径
tag_to_add = ""  # 要添加的标签


def add_tag_to_file(file_path):
    with open(file_path, "r+", encoding="utf-8") as file:
        content = file.readlines()

        # 检查文件开头是否有 --- 分隔符
        if content[0].strip() == "---":
            # 检查是否已存在 dg-publish 设置
            for i, line in enumerate(content[1:]):
                if line.strip() == "---":
                    break
                if "dg-publish:" in line:
                    if "dg-publish: true" in line:
                        print(f"File already has dg-publish: true in: {file_path}")
                        return
                    elif "dg-publish: false" in line:
                        print(f"File has dg-publish: false, not modifying: {file_path}")
                        return

            # 在第二行插入 dg-publish: true
            content.insert(1, "dg-publish: true\n")
            content.insert(2, "\n")  # 添加一个空行以保持格式
        else:
            # 如果文件开头没有 --- 分隔符，则添加完整的 frontmatter
            content = ["---\n", "dg-publish: true\n", "\n", "---\n"] + content

        # 重写文件内容
        file.seek(0)
        file.writelines(content)
        file.truncate()
        print(f"Added dg-publish: true to: {file_path}")


def add_tag_to_markdown_files(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if filename.endswith(".md"):
                file_path = os.path.join(root, filename)
                add_tag_to_file(file_path)


# 执行添加操作
add_tag_to_markdown_files(path)
