from flask import Flask, render_template, request, redirect
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


@app.route("/admin")
def admin():
    posts = Post.query.all()
    return render_template("admin.html", posts=posts)


@app.route("/create", methods=["GET", "POST"])
def create():
    # リクエストのメソッドの判別
    if request.method == "POST":

        # リクエストできた情報の判別
        title = request.form.get("title")
        body = request.form.get("body")

        # 情報の保存
        post = Post(title=title, body=body)
        db.session.add(post)
        db.session.commit()
        return redirect("/admin")

    elif request.method == "GET":
        return render_template("create.html", method="GET")


""" pythonコマンド
>>> from myapp import app, db
>>> with app.app_context():
...     db.create_all() # 最初にTabキーを入れる
"""
