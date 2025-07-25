from ..nodes import HTMLNode
from ..functions import markdown_to_html_node, extract_title

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    with open(from_path) as f:
        markdown = f.read()
    
    with open(template_path) as f:
        template = f.read()
    
    html = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)
    
    # THE FIX IS HERE:
    # 1. Create the destination directory using pathlib if it doesn't exist.
    #    dest_path.parent gets the directory (e.g., 'public/').
    #    mkdir() creates it. `parents=True` creates any needed parent folders,
    #    and `exist_ok=True` prevents an error if it's already there.
    dest_path.parent.mkdir(parents=True, exist_ok=True)
    
    # 2. Open the destination file in 'w' (write) mode to write the content.
    with open(dest_path, "w") as f:
        f.write(template)