from flask import Flask, render_template, url_for
import os
import markdown
from datetime import datetime

app = Flask(__name__)

def get_blog_posts():
    posts = []
    content_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'contents')
    for filename in os.listdir(content_dir):
        if filename.endswith(".md"):
            # Extract title and date from filename
            title = os.path.splitext(filename)[0].replace("-", " ").title()
            date_str = filename.split("-")[0]
            posts.append({
                'filename': filename,
                'title': title,
                'date': date_str
            })
    # Sort posts by date, newest first
    posts.sort(key=lambda x: x['date'], reverse=True)
    return posts

@app.route('/')
def hello():
    posts = get_blog_posts()
    return render_template('index.html', posts=posts)

@app.route('/post/<filename>')
def post(filename):
    content_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'contents')
    filepath = os.path.join(content_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        html_content = markdown.markdown(content)
    title = os.path.splitext(filename)[0].replace("-", " ").title()
    return render_template('post.html', post={'title': title, 'html_content': html_content})

@app.route('/test')
def test():
    return 'Test'

@app.route('/result')
def result():
   dict = {'phy':50,'che':60,'maths':70}
   return render_template('result.html', result = dict)

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/trigger', methods=['POST'])
def trigger():
    os.system(f'curl -X POST -H "Accept: application/vnd.github.v3+json" -H "Authorization: token $GHTOKEN" https://api.github.com/repos/inakimaldive/micro-allinone2-port/dispatches -d \'{{"event_type":"create-dated-file"}}\'')
    return 'OK'
