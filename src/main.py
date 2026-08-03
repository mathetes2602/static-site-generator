import os
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

def generate_page(from_path, template_path, dest_path):
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
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(template)

def main():
    main_dir = os.path.abspath("./")
    content_path = os.path.join(main_dir, "content", "index.md")
    template_path = os.path.join(main_dir, "template.html")
    public_path = os.path.join(main_dir, "public")
    dest_path = os.path.join(public_path, "index.html")
    static_path = os.path.join(main_dir, "static")
    copy_files(static_path, public_path)
    generate_page(content_path, template_path, dest_path)  

main()