from ..functions import generate_page

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for md_file in dir_path_content.rglob("*.md"):
        output_path = dest_dir_path / md_file.relative_to(dir_path_content).with_suffix('.html')
        generate_page(md_file, template_path, output_path)