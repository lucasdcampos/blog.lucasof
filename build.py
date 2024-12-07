from core.markdown_processor import process_markdown_files
from core.index_generator import generate_index
from core.copy_static import copy_static_files

STATIC_DIR = "static/"
INPUT_DIR = "posts/"
OUTPUT_DIR = "build/posts/"
INDEX_OUTPUT_PATH = "build/index.html"
TEMPLATE_PATH = "post_base.html"

def main():

    print("Copying static files...")
    try:
        copy_static_files(STATIC_DIR, "build/")
    except Exception as e:
        print(f"Erro: {e}")

    print("Processing markdown files...")
    posts = process_markdown_files(INPUT_DIR, OUTPUT_DIR)
    
    print("Generating index.html...")
    generate_index(posts, INDEX_OUTPUT_PATH)
    
    print("Done!")

if __name__ == "__main__":
    main()
