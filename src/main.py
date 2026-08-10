import os
import sys
import shutil
import re
from block_functions import markdown_to_html_node

def extract_title(markdown: str) -> str:
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise Exception("no h1 header found")

def copy_files(origin, destination):
    if os.path.exists(destination):
        shutil.rmtree(destination)

    os.mkdir(destination)
    dir_items = os.listdir(origin)
    for item in dir_items:
        item_path = os.path.join(origin, item)
        if os.path.isfile(item_path):
            shutil.copy(item_path, os.path.join(destination, item))
        if os.path.isdir(item_path):
            copy_files(item_path, os.path.join(destination, item))

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown_content = None
    with open(from_path, encoding="utf-8") as f:
        content = f.read()
    template = None
    with open(template_path, encoding="utf-8")as f:
        template = f.read()
    html_content = markdown_to_html_node(content).to_html()
    title = extract_title(content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html_content)
    template = template.replace('href="/', f'href="{basepath}')
    template = template.replace('src="/', f'src="{basepath}')

    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)
    dir_items = os.listdir(dir_path_content)
    for item in dir_items:
        item_origin_path = os.path.join(dir_path_content, item)
        item_dest_path = os.path.join(dest_dir_path, item)
        if os.path.isfile(item_origin_path):
            new_file_name = os.path.join(dest_dir_path, item[:-2] + "html")
            generate_page(item_origin_path, template_path, new_file_name, basepath)
        if os.path.isdir(item_origin_path):
            generate_pages_recursive(item_origin_path, template_path, item_dest_path, basepath)

def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    main_dir = os.path.abspath("./")
    content_path = os.path.join(main_dir, "content")
    template_path = os.path.join(main_dir, "template.html")
    public_path = os.path.join(main_dir, "docs")
    dest_path = os.path.join(public_path, "index.html")
    static_path = os.path.join(main_dir, "static")
    copy_files(static_path, public_path)
    generate_pages_recursive(content_path, template_path, public_path, basepath)

main()