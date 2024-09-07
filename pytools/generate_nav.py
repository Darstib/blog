import os
import shutil


def generate_yaml(path, base_path, root_folder):
    yaml_content = []

    # 获取子文件夹并按字母顺序排序
    sub_folders = sorted(
        [
            f
            for f in os.listdir(path)
            if os.path.isdir(os.path.join(path, f)) and f != ".git"
        ]
    )

    # 如果当前文件夹为空，返回空
    if not sub_folders and not any(f.endswith(".md") for f in os.listdir(path)):
        return yaml_content

    # 处理子文件夹，优先递归检查
    for sub_folder in sub_folders:
        folder_path = os.path.join(path, sub_folder)
        folder_content = generate_yaml(folder_path, base_path, root_folder)
        # 如果子文件夹有内容，直接作为该文件夹的子项
        if folder_content:
            # 如果子文件夹只有一个子项并且是单个 Markdown 文件，则作为该文件夹的内容
            if (
                len(folder_content) == 1
                and isinstance(folder_content[0], str)
                and folder_content[0].count(":") == 1
            ):
                yaml_content.append(
                    f"{sub_folder}: {folder_content[0].split(': ', 1)[1]}"
                )
            else:
                yaml_content.append({f"{sub_folder}": folder_content})

    # 获取 markdown 文件，按顺序排序
    markdown_files = sorted([f for f in os.listdir(path) if f.endswith(".md")])

    # 处理 README.md，作为首要文件
    if "README.md" in markdown_files:
        item_path = os.path.join(path, "README.md")
        relative_path = os.path.relpath(item_path, base_path)
        full_path = f"{root_folder}/{relative_path}"
        yaml_content.insert(0, f"{full_path}")
        markdown_files.remove("README.md")

    # 处理其他 Markdown 文件
    files = []
    for item in markdown_files:
        item_path = os.path.join(path, item)
        relative_path = os.path.relpath(item_path, base_path)
        full_path = f"{root_folder}/{relative_path}"
        file_name_without_extension = os.path.splitext(item)[0]
        files.append(f"{file_name_without_extension}: {full_path}")

    # 对 Markdown 文件排序并加入内容
    files.sort(key=lambda x: os.path.basename(x).lower())
    yaml_content.extend(files)

    return yaml_content


def format_yaml(data, indent=0):
    yaml_str = ""
    for item in data:
        if isinstance(item, dict):
            key = next(iter(item))
            # 添加冒号来标识文件夹，不为其内容额外加 `- `
            yaml_str += " " * indent + f"- {key}:\n"
            yaml_str += format_yaml(item[key], indent + 2)
        else:
            # 只为字符串项加 `- `
            if ": " in item:
                yaml_str += " " * indent + f"- {item}\n"
            else:
                yaml_str += " " * indent + f"- {item}\n"
    return yaml_str


base_path = "/home/qssg/webpage/blog/docs/note/cs188/note"
root_folder = os.path.basename(base_path)
yaml_data = generate_yaml(base_path, base_path, root_folder)
yaml_str = format_yaml(yaml_data)

with open("result.txt", "w") as f:
    f.write(yaml_str)

print("YAML content has been written to result.txt")
