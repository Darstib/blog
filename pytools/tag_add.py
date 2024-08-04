import os

# 目标文件夹路径
path = "/mnt/d/a_ob/test"  # 替换为文件夹路径
tag_to_add = "test"  # 要添加的标签


def add_tag_to_file(file_path):
    with open(file_path, "r+", encoding="utf-8") as file:
        content = file.readlines()

        # 检查是否已存在该标签
        tag_line = f"- {tag_to_add}\n"
        if any(tag_line.strip() in line for line in content):
            print(f"Tag '{tag_to_add}' already exists in: {file_path}")
            return

        # 找到合适的位置添加标签
        for i, line in enumerate(content):
            if line.strip() == "tags:":
                # 在tags后添加标签
                content.insert(i + 1, tag_line)
                break
        else:
            # 如果没有找到tags部分，则在文件末尾添加
            content.append("\ntags:\n" + tag_line)

        # 重写文件内容
        file.seek(0)
        file.writelines(content)
        file.truncate()
        print(f"Added tag '{tag_to_add}' in: {file_path}")


def add_tag_to_markdown_files(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if filename.endswith(".md"):
                file_path = os.path.join(root, filename)
                add_tag_to_file(file_path)


# 执行添加操作
add_tag_to_markdown_files(path)
