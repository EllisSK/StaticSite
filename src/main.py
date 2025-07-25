import pathlib
from .nodes import TextNode, TextType
from .functions import copy_static, generate_page

def main():
    current_path = pathlib.Path.cwd()
    index_path =  current_path / "content" / "index.md"
    template_path = current_path / "template.html"
    output_path = current_path / "public" / "index.html"
    
    copy_static()
    generate_page(index_path, template_path, output_path)

main()