from myapp_001 import app
from flask import render_template, request, redirect, url_for
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


@app.route("/result")
def result():
    return render_template("result.html")


@app.route("/register", methods=["POST"])
def register():
    name = request.form["name"]
    age = request.form["age", ""]
    if age and age != "不明":
        age = str(age) + "歳"
    gender = request.form["gender"]
    occupation = request.form["occupation"]
    message = request.form["message"]

    with sqlite3.connect(DATABASE) as con:
        con.execute("INSERT INTO profile VALUES(?, ?, ?, ?, ?)", [name, age, gender, occupation, message])
        con.commit()
    return redirect(url_for("index"))
