import os
import markdown
import yaml
from core.post import Post
from datetime import datetime

# Function to extract metadata from YAML front matter
def extract_metadata(content):
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) > 2:
            metadata = yaml.safe_load(parts[1])
            markdown_content = parts[2].strip()
            return metadata, markdown_content
    return {}, content

# Function to generate the HTML of a post using post_base.html
def generate_post_html(post, template_path):
    if not os.path.exists(template_path):
        raise FileNotFoundError(f"Template {template_path} not found.")

    # Load the template from the post_base.html file
    with open(template_path, 'r', encoding='utf-8') as template_file:
        post_template = template_file.read()

    # Replace the placeholders with the post content
    post_html = post_template.replace("{{ post_title }}", post.title)
    post_html = post_html.replace("{{ post_content }}", post.html_content)
    post_html = post_html.replace("{{ post_date }}", str(post.post_date))

    return post_html

# Function to process the Markdown files
def process_markdown_files(input_dir, output_dir, template_path="post_base.html"):
    if not os.path.exists(input_dir):
        raise FileNotFoundError(f"The directory '{input_dir}' was not found.")

    os.makedirs(output_dir, exist_ok=True)
    posts = []

    for filename in os.listdir(input_dir):
        if filename.endswith(".md"):
            md_path = os.path.join(input_dir, filename)
            with open(md_path, 'r', encoding='utf-8') as md_file:
                content = md_file.read()

            # Extract metadata and Markdown content
            metadata, markdown_content = extract_metadata(content)

            # Convert the Markdown content to HTML
            html_content = markdown.markdown(markdown_content)

            # Set default values for the metadata
            title = metadata.get("title", "Untitled")
            tags_str = metadata.get("tags", "")
            tags = tags_str.split(", ") if tags_str else []

            post_date_str = metadata.get("date", "unknown")

            # Check if post_date_str is already a datetime object
            if isinstance(post_date_str, datetime):
                post_date = post_date_str
            elif isinstance(post_date_str, str):
                try:
                    # Try to convert the string to datetime
                    # In case it has time: "YYYY-MM-DD HH:MM:SS"
                    post_date = datetime.strptime(post_date_str, "%Y-%m-%d %H:%M:%S")
                except ValueError:
                    try:
                        # In case the date is only the day: "YYYY-MM-DD"
                        post_date = datetime.strptime(post_date_str, "%Y-%m-%d")
                        # If it's only the day, set the current time
                        post_date = post_date.replace(hour=datetime.now().hour, minute=datetime.now().minute, second=datetime.now().second)
                    except ValueError:
                        # If the date cannot be converted, use the current date
                        post_date = datetime.now()
            else:
                # If post_date_str is neither string nor datetime, use the current date
                post_date = datetime.now()

            # Create the Post object
            post = Post(
                filename=filename,
                markdown_content=markdown_content,
                html_content=html_content,
                title=title,
                tags=tags,
                post_date=post_date,
            )

            # Generate the final HTML using the template
            final_html = generate_post_html(post, template_path)

            # Save the HTML file in the output directory
            output_path = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}.html")
            with open(output_path, 'w', encoding='utf-8') as html_file:
                html_file.write(final_html)

            posts.append(post)

    # Sort the posts by date (most recent first)
    posts.sort(key=lambda post: post.post_date, reverse=True)

    return posts


