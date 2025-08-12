from myapp_001 import app
from flask import render_template, request, redirect, url_for, flash
import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(BASE_DIR, "database.db")


@app.route("/")
def index():
    with sqlite3.connect(DATABASE) as con:
        db_profiles = con.execute("SELECT * FROM profile").fetchall()

    profs = [
        {"name": row[0], "age": row[1], "gender": row[2], "occupation": row[3], "message": row[4]}
        for row in db_profiles
    ]
    return render_template("index.html", profs=profs)


@app.route("/form")
def form():
    return render_template("form.html")


@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name", "").strip()
    age = request.form.get("age", "").strip()
    gender = request.form.get("gender", "").strip()
    occupation = request.form.get("occupation", "").strip()
    message = request.form.get("message", "").strip()

    # 簡易バリデーション
    if not all([name, age, gender, occupation, message]):
        flash("全ての項目を入力してください。")
        return redirect(url_for("form"))

    if not age.isdigit():
        flash("年齢は数字で入力してください。")
        return redirect(url_for("form"))

    if len(message) > 100:
        flash("100文字以内で入力してください。")
        return redirect(url_for("form"))

    age = age + "歳"

    # ここでDBに保存...
    # insert処理

    with sqlite3.connect(DATABASE) as con:
        con.execute("INSERT INTO profile VALUES(?, ?, ?, ?, ?)", [name, age, gender, occupation, message])
        con.commit()
    return redirect(url_for("index"))
