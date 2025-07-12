from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pytz

app = Flask(__name__)

db = SQLAlchemy()
DB_INFO = {
    "user": "postgres",
    "password": "aaaa",
    "host": "172.20.17.29",
    "port": "5432",
    "name": "postgres",
}

SQLALCHEMY_DATABASE_URI = "postgresql+psycopg://{user}:{password}@{host}:{port}/{name}".format(**DB_INFO)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


# 日本時間の現在時刻を返す関数
def tokyo_now():
    return datetime.now(pytz.timezone("Asia/Tokyo"))


class Post(db.Model):  # type: ignore
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    body = db.Column(db.String(1000), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=tokyo_now)


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


""" pythonコマンド
>>> from myapp import app, db
>>> with app.app_context():
...     db.create_all() # 最初にTabキーを入れる
"""
