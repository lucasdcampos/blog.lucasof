from datetime import datetime

class Post:
    def __init__(self, filename, markdown_content, html_content, title, tags, post_date):
        self.filename = filename
        self.markdown_content = markdown_content
        self.html_content = html_content
        self.title = title
        self.tags = tags
        self.post_date = post_date or datetime.now().strftime("%Y-%m-%d %H:%M:%S")
