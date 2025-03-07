import os
import shutil

from markdown_blocks import markdown_to_html_node


def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("no title found")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    if not dest_path:
        raise ValueError

    # Read the markdown file at from_path and store the contents in a variable.
    content=''
    with open(from_path, 'r', encoding='utf-8') as file:
        content = file.read()

    #Read the template file at template_path and store the contents in a variable.
    template=''
    with open(template_path, 'r', encoding='utf-8') as file:
        template = file.read()
  
    #Use your markdown_to_html_node function and .to_html() method to convert the markdown file to an HTML string.
    html_content = markdown_to_html_node(content).to_html()

    #Use the extract_title function to grab the title of the page.
    title = extract_title(content)

    #Replace the {{ Title }} and {{ Content }} placeholders in the template with the HTML and title you generated.
    final_html = template.replace('{{ Title }}', title)
    final_html = final_html.replace('{{ Content }}', html_content)

    #Write the new full HTML page to a file at dest_path. Be sure to create any necessary directories if they don't exist.
    dest_dir_path = os.path.dirname(dest_path)
    
    os.makedirs(dest_dir_path, exist_ok=True)
    
    with open(dest_path, 'w', encoding='utf-8') as file:
        file.write(final_html)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for item in os.listdir(dir_path_content):
        item_path = os.path.join(dir_path_content, item)
        new_dir = os.path.join(dest_dir_path, item)
        
        if os.path.isdir(item_path):
            #create a new file in the home destiniation
            if not os.path.exists(new_dir):
                os.mkdir(new_dir)           
            
            generate_pages_recursive(item_path, template_path, new_dir)
            continue

        if item.endswith(".md"):
            new_dir = new_dir[:-3]
            new_dir += '.html'
            generate_page(item_path, template_path, new_dir)


