import os

# 目标文件夹路径
path = "/mnt/d/a_ob/docs/CTF/"  # 替换为文件夹路径
attribute_to_add = "level: friend"  # 要添加的属性和值，格式为 "属性名: 值"


def add_attribute_to_file(file_path, attribute):
    with open(file_path, "r+", encoding="utf-8") as file:
        content = file.readlines()

        # 解析属性名和值
        attribute_name, attribute_value = attribute.split(": ", 1)
        attribute_line = f"{attribute_name}: {attribute_value}"

        # 检查文件开头是否有 --- 分隔符
        if content[0].strip() == "---":
            # 检查是否已存在属性
            for i, line in enumerate(content[1:]):
                if line.strip() == "---":
                    break
                if line.strip().startswith(attribute_name + ":"):
                    if line.strip() == attribute_line.strip():
                        print(
                            f"File already has {attribute_line.strip()} in: {file_path}"
                        )
                        return
                    else:
                        print(f"File has {line.strip()}, not modifying: {file_path}")
                        return

            # 在第二行插入属性
            content.insert(1, attribute_line)
            content.insert(2, "\n")  # 添加一个空行以保持格式
        else:
            # 如果文件开头没有 --- 分隔符，则添加完整的 frontmatter
            content = ["---\n", attribute_line, "\n", "---\n"] + content

        # 重写文件内容
        file.seek(0)
        file.writelines(content)
        file.truncate()
        print(f"Added {attribute_line.strip()} to: {file_path}")


def add_attribute_to_markdown_files(folder_path, attribute):
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if filename.endswith(".md"):
                file_path = os.path.join(root, filename)
                add_attribute_to_file(file_path, attribute)


# 执行添加操作
add_attribute_to_markdown_files(path, attribute_to_add)
