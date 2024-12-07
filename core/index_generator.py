import os

def generate_index(posts, output_path, template_path="html/index.html"):
    # Load the content of the index.html template file
    if not os.path.exists(template_path):
        raise FileNotFoundError(f"Template {template_path} not found.")
    
    with open(template_path, 'r', encoding='utf-8') as template_file:
        index_template = template_file.read()

    # Replace the {{ blog_posts }} variable with the list of posts
    blog_posts_html = "\n".join(
        f'<p>{post.post_date.strftime("%Y-%m-%d %H:%M")}<p><a href="posts/{os.path.splitext(post.filename)[0]}.html">{post.title}</a>'
        for post in posts
        if not post.filename.startswith('_')
    )

    index_content = index_template.replace("{{ blog_posts }}", blog_posts_html)
    footer = open("html/footer.html", "r")
    index_content = index_content.replace("{{ footer }}", footer.read())

    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Save the generated content to the index.html file in the build/ directory
    with open(output_path, 'w', encoding='utf-8') as index_file:
        index_file.write(index_content)
