import os
import re

import yaml
from jinja2 import Template
from rich import print

from mkdocs.config import config_options
from mkdocs.plugins import BasePlugin
from mkdocs.structure.pages import Page
from mkdocs.utils import copy_file

from typing import Any, Dict

from .utils import get_statistics, get_update_time

PLUGIN_DIR = os.path.dirname(os.path.realpath(__file__))
TEMPLATE_DIR = os.path.join(PLUGIN_DIR, "templates/toc.html")

with open(TEMPLATE_DIR, "r", encoding="utf-8") as file:
    TEMPLATE = file.read()

class TocPlugin(BasePlugin):
    config_scheme = (
        ("enabled", config_options.Type(bool, default=True)),
        ("ignore_commits", config_options.Type(list, default=[])),
    )

    enabled = True

    def on_config(self, config: config_options.Config, **kwargs) -> Dict[str, Any]:
        if not self.enabled:
            return config
        
        if not self.config.get("enabled"):
            return config
        
        config["extra_css"] = ["css/toc_extra.css"] + config["extra_css"]
    
    def on_page_markdown(
        self, markdown: str, page: Page, config: config_options.Config, files, **kwargs
    ) -> str:
        if not self.enabled or not self.config.get("enabled"):
            return markdown

        def check_toc_txt(toc_txt: str) -> None:
            try:
                # 如果检测到第一行不以 '-' 开头则抛出异常
                if not toc_txt.lstrip().startswith("-"):
                    raise ValueError("Markdown TOC 格式错误：必须以 '-' 开头")
            except Exception as e:
                raise ValueError(f"Markdown TOC 解析失败：{e}")

        base_path = os.path.dirname(page.file.abs_src_path)
        if "{{ begin_toc }}" in markdown and "{{ end_toc }}" in markdown:
            toc_txt = markdown.split("{{ begin_toc }}")[1].split("{{ end_toc }}")[0]
            check_toc_txt(toc_txt)
            toc_txt = self._markdown_to_yaml(toc_txt)

        elif "{{ BEGIN_TOC }}" in markdown and "{{ END_TOC }}" in markdown:
            toc_txt = markdown.split("{{ BEGIN_TOC }}")[1].split("{{ END_TOC }}")[0]
            check_toc_txt(toc_txt)
        else:
            return markdown

        toc = yaml.load(toc_txt, Loader=yaml.FullLoader)
        toc_items = self._get_toc_items(toc, base_path)
        toc_html = Template(TEMPLATE).render(items=toc_items)
        markdown = re.sub(
            r"\{\{ BEGIN_TOC \}\}.*\{\{ END_TOC \}\}",
            toc_html,
            markdown,
            flags=re.IGNORECASE | re.DOTALL,
        )

        return markdown

    def on_post_build(self, config: Dict[str, Any], **kwargs) -> None:
        if not self.enabled:
            return
        
        if not self.config.get("enabled"):
            return
        
        files = ["css/toc_extra.css"]
        for file in files:
            dest_file_path = os.path.join(config["site_dir"], file)
            src_file_path = os.path.join(PLUGIN_DIR, file)
            assert os.path.exists(src_file_path)
            copy_file(src_file_path, dest_file_path)
    
    def _get_toc_items(self, toc: dict, base: str) -> list:
        ret = []
        for i, part in enumerate(toc):
            item = dict()
            item['n'] = i
            title = list(part.keys())[0]
            if "[note]" in title:
                item['note'] = True
                title = title.replace("[note]", "")
            else:
                item['note'] = False
            item['title'] = title
            details = []
            for d in part[list(part.keys())[0]]:
                key = list(d.keys())[0]
                value = d[key]
                if key == "index":
                    item['link'] = value
                    continue
                detail = dict()
                t = key
                detail['note'] = False
                detail['lab'] = False
                if "[note]" in t:
                    detail['note'] = True
                    t = t.replace("[note]", "")
                if "[lab]" in t:
                    detail['lab'] = True
                    t = t.replace("[lab]", "")
                detail['title'] = t
                detail['link'] = value
                detail['words'], detail['codes'], detail['read_time'] = get_statistics(value, base)
                detail['update_time'] = get_update_time(value, base, self.config.get("ignore_commits", []))
                if "🔒" in t:
                    detail['lock'] = True
                details.append(detail)
            details.sort(key=lambda x: x['update_time'], reverse=True)
            item['contents'] = details
            ret.append(item)
        return ret

    # def _markdown_to_yaml(self, markdown: str) -> str:
    #     # 用于处理链接的方法
    #     def process_link(link: str) -> str:
    #         link = link.strip()
    #         path_parts = link.split('/')
    #         if not path_parts:
    #             return link
    #         last = path_parts[-1]
    #         if last.lower() in ("readme.md", "index.md"):
    #             # 舍弃最后的文件名，确保以 "/" 结尾
    #             dir_path = '/'.join(path_parts[:-1])
    #             if dir_path and not dir_path.endswith('/'):
    #                 dir_path += '/'
    #             return dir_path
    #         else:
    #             # 去掉文件扩展名
    #             if '.' in last:
    #                 path_parts[-1] = last.rsplit('.', 1)[0]
    #             return '/'.join(path_parts)

    #     # 按行解析 markdown
    #     lines = markdown.splitlines()
    #     result = []
    #     current_top = None

    #     # 匹配 markdown 链接行 的正则模式
    #     link_pattern = re.compile(r'\[\s*([^\]]+?)\s*\]\s*\(\s*([^)]+?)\s*\)')

    #     for line in lines:
    #         if not line.strip():
    #             continue
    #         # 判断是否为顶级行：非缩进行（即开头没有空白字符或仅有 '-'）
    #         if re.match(r'^\s*-\s*\[', line) and (len(line) == len(line.lstrip())):
    #             m = link_pattern.search(line)
    #             if m:
    #                 label, link = m.groups()
    #                 processed_link = process_link(link) if link else ''
    #                 # 顶级行以 "index" 作为键保存链接
    #                 current_top = { label: [ { "index": processed_link } ] }
    #                 result.append(current_top)
    #             else:
    #                 # 即使没有链接，也要保留 label
    #                 label = line.split('[')[1].split(']')[0].strip()
    #                 current_top = { label: [ { "index": '' } ] }
    #                 result.append(current_top)
    #                 continue
    #         else:
    #             # 视为子项，需要属于最近一个顶级
    #             m = link_pattern.search(line)
    #             if m and current_top is not None:
    #                 sub_label, sub_link = m.groups()
    #                 processed_link = process_link(sub_link) if sub_link else ''
    #                 # 直接以 [] 中的内容作为 key
    #                 for key in current_top:
    #                     current_top[key].append({ sub_label: processed_link })
    #             else:
    #                 # 即使没有链接，也要保留 label
    #                 if current_top is not None and '[' in line and ']' in line:
    #                     sub_label = line.split('[')[1].split(']')[0].strip()
    #                     for key in current_top:
    #                         current_top[key].append({ sub_label: '' })
    #                 continue

    #     # 使用 yaml.dump 转换为 YAML 字符串，保持键的顺序
    #     return yaml.dump(result, allow_unicode=True, sort_keys=False)


    def _markdown_to_yaml(self, markdown: str) -> str:
        import re
        # 用于处理链接的方法
        def process_link(link: str) -> str:
            link = link.strip()
            path_parts = link.split('/')
            if not path_parts:
                return link
            last = path_parts[-1]
            if last.lower() in ("readme.md", "index.md"):
                # 舍弃最后的文件名，确保以 "/" 结尾
                dir_path = '/'.join(path_parts[:-1])
                if dir_path and not dir_path.endswith('/'):
                    dir_path += '/'
                return dir_path
            else:
                # 去掉文件扩展名
                if '.' in last:
                    path_parts[-1] = last.rsplit('.', 1)[0]
                return '/'.join(path_parts)

        # 按行解析 markdown
        lines = markdown.splitlines()
        result = []
        current_top = None

        # 匹配 markdown 链接行 的正则模式
        link_pattern = re.compile(r'\[\s*([^\]]+?)\s*\]\s*\(\s*([^)]+?)\s*\)')

        for line in lines:
            if not line.strip():
                continue

            # 判断是否为顶级行：非缩进行（即开头没有空白字符或仅有 '-'）
            if re.match(r'^\s*-\s*', line) and (len(line) == len(line.lstrip())):
                # 尝试匹配链接
                m = link_pattern.search(line)
                if m:
                    label, link = m.groups()
                    processed_link = process_link(link) if link else ''
                    current_top = { label: [ { "index": processed_link } ] }
                    result.append(current_top)
                else:
                    # 如果没有链接，则提取行中的文本作为标签
                    label = line.lstrip().lstrip('-').strip()
                    current_top = { label: [ { "index": '' } ] }
                    result.append(current_top)
                continue
            else:
                # 视为子项，需要属于最近一个顶级
                m = link_pattern.search(line)
                if m and current_top is not None:
                    sub_label, sub_link = m.groups()
                    processed_link = process_link(sub_link) if sub_link else ''
                    for key in current_top:
                        current_top[key].append({ sub_label: processed_link } )
                else:
                    # 如果没有链接，则提取行中的文本作为标签
                    sub_label = line.lstrip().lstrip('-').strip()
                    if current_top is not None:
                        for key in current_top:
                            current_top[key].append({ sub_label: '' })
                    continue

        # 使用 yaml.dump 转换为 YAML 字符串，保持键的顺序
        return yaml.dump(result, allow_unicode=True, sort_keys=False)