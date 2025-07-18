from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_migrate import Migrate
import pytz
import os

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

# ---データベース変更
# $ python3 -m pip install types-Flask-Migrate
# $ flask --app myapp db init // migrationsフォルダが生成される
# $ flask --app myapp db migrate -m "add img_name" // commit
migrate = Migrate(app, db)


# 日本時間の現在時刻を返す関数
def tokyo_now():
    return datetime.now(pytz.timezone("Asia/Tokyo"))


# ---データベースに追加
class Post(db.Model):  # type: ignore
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    body = db.Column(db.String(1000), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=tokyo_now)
    img_name = db.Column(db.String(100), nullable=True)


# ---/adminの処理
@app.route("/admin")
def admin():
    posts = Post.query.all()
    return render_template("admin.html", posts=posts)


# ---記事の新規登録---
@app.route("/create", methods=["GET", "POST"])
def create():
    # リクエストのメソッドの判別
    if request.method == "POST":

        # リクエストできた情報の判別
        title = request.form.get("title")
        body = request.form.get("body")

        # 画像情報の取得
        file = request.files["img"]
        filename = file.filename
        ext = os.path.splitext(filename)[1].lower()

        if ext not in [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"]:
            return redirect("/create")

        # 情報の保存
        post = Post(title=title, body=body, img_name=filename)

        # 画像の保存
        save_path = os.path.join(app.static_folder, "img", filename)
        file.save(save_path)

        db.session.add(post)
        db.session.commit()
        return redirect("/admin")

    elif request.method == "GET":
        return render_template("create.html", method="GET")


# ---記事の更新---
@app.route("/<int:post_id>/update", methods=["GET", "POST"])
def update(post_id):
    post = Post.query.get(post_id)
    if request.method == "POST":
        # 記事の更新
        post.title = request.form.get("title")
        post.body = request.form.get("body")
        db.session.commit()
        return redirect("/admin")

    elif request.method == "GET":
        return render_template("update.html", post=post)


# ---記事の削除---
@app.route("/<int:post_id>/delete")
def delete(post_id):
    post = Post.query.get(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect("/admin")


""" pythonコマンド
>>> from myapp import app, db
>>> with app.app_context():
...     db.create_all() # 最初にTabキーを入れる
"""
