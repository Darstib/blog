import os
import shutil


def generate_yaml(path, base_path, root_folder):
    yaml_content = []
    files = []

    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            # 跳过 .git 文件夹
            if item == ".git":
                # 删除 .git 文件夹
                shutil.rmtree(item_path)
                continue

            # 检查子文件夹是否包含 Markdown 文件
            has_markdown = any(f.endswith(".md") for f in os.listdir(item_path))
            if has_markdown:
                sub_content = generate_yaml(item_path, base_path, root_folder)
                yaml_content.append({f"{item}:": sub_content})
        elif os.path.isfile(item_path) and item.endswith(".md"):
            relative_path = os.path.relpath(item_path, base_path)
            full_path = f"{root_folder}/{relative_path}"
            if item == "README.md":
                yaml_content.insert(0, f"- {full_path}")
            else:
                file_name_without_extension = os.path.splitext(item)[0]
                files.append(f"- {file_name_without_extension}: {full_path}")

    files.sort(key=lambda x: os.path.basename(x))
    yaml_content.extend(files)

    return yaml_content


def format_yaml(data, indent=0):
    yaml_str = ""
    for item in data:
        if isinstance(item, dict):
            key = next(iter(item))
            yaml_str += " " * indent + f"- {key}\n"
            yaml_str += format_yaml(item[key], indent + 2)
        else:
            yaml_str += " " * indent + f"{item}\n"
    return yaml_str


base_path = "/home/qssg/webpage/blog/docs/note"
root_folder = os.path.basename(base_path)
yaml_data = generate_yaml(base_path, base_path, root_folder)
yaml_str = format_yaml(yaml_data)

with open("result.txt", "w") as f:
    f.write(yaml_str)

print("YAML content has been written to result.txt")
