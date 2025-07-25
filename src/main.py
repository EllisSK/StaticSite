import pathlib
from .nodes import TextNode, TextType
from .functions import copy_static, generate_page, generate_pages_recursive

def main():
    current_path = pathlib.Path.cwd()
    content_path =  current_path / "content"
    template_path = current_path / "template.html"
    output_path = current_path / "public"
    
    copy_static()
    generate_pages_recursive(content_path, template_path, output_path)

main()