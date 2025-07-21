from flask import Flask, render_template
import os
from dotenv import load_dotenv
import markdown # Added import

load_dotenv()

app = Flask(__name__)

def get_blog_posts():
    posts = []
    content_dir = os.path.join(app.root_path, '..', 'contents') # Path to contents directory
    for filename in os.listdir(content_dir):
        if filename.endswith(".md"):
            filepath = os.path.join(content_dir, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                html_content = markdown.markdown(content)
                posts.append({'filename': filename, 'html_content': html_content})
    return posts

@app.route('/')
def hello():
    posts = get_blog_posts()
    return render_template('index.html', posts=posts)


@app.route('/test')
def test():
    return 'Test'

@app.route('/result')
def result():
   dict = {'phy':50,'che':60,'maths':70}
   return render_template('result.html', result = dict)

@app.route('/trigger', methods=['POST'])
def trigger():
    os.system(f"""curl -X POST -H "Accept: application/vnd.github.v3+json" -H "Authorization: token $GHTOKEN" https://api.github.com/repos/IgnatMaldive/micro-allinone2/dispatches -d '{{"event_type":"create-dated-file"}}'""")
    return 'OK'
