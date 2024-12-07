import os

def generate_index(posts, output_path, template_path="index.html"):
    # Load the content of the index.html template file
    if not os.path.exists(template_path):
        raise FileNotFoundError(f"Template {template_path} not found.")
    
    with open(template_path, 'r', encoding='utf-8') as template_file:
        index_template = template_file.read()

    # Replace the {{ blog_posts }} variable with the list of posts
    blog_posts_html = "\n".join(
        f'<a href="posts/{os.path.splitext(post.filename)[0]}.html">{post.title}<br>{post.post_date.strftime("%Y-%m-%d %H:%M")}</a><br>'
        for post in posts
        if not post.filename.startswith('_')
    )

    index_content = index_template.replace("{{ blog_posts }}", blog_posts_html)

    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Save the generated content to the index.html file in the build/ directory
    with open(output_path, 'w', encoding='utf-8') as index_file:
        index_file.write(index_content)
