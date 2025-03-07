import os
import sys
import shutil

from copystatic import copy_files_recursive
from gencontent import generate_page, generate_pages_recursive

dir_path_static = "./static"
#dir_path_public = "./public" # used in testing and building
dir_path_docs = './docs'
dir_path_content = "./content"
template_path = "template.html"

def main(args):
    print(args)
    basepath = '/'
    if len(args) >= 2:
        basepath = args[1]

    print("Deleting public directory...")

    if os.path.exists(dir_path_docs):
        shutil.rmtree(dir_path_docs)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_docs)

    print("Generating pages...")
    generate_pages_recursive(dir_path_content, template_path, dir_path_docs, basepath)


main(sys.argv)
