from flask import Flask, render_template

app = Flask(__name__)


@app.route("/<int:number>")
def hello_world(number):
    posts = [
        {"title": "記事のタイトル1", "body": "記事の内容", "created_at": "2024-06-17"},
        {"title": "記事のタイトル2", "body": "記事の内容", "created_at": "2024-06-17"},
        {"title": "記事のタイトル3", "body": "記事の内容", "created_at": "2024-06-17"},
        {"title": "記事のタイトル4", "body": "記事の内容", "created_at": "2024-06-17"},
    ]
    post = posts[number]
    return render_template("admin.html", post=post)
