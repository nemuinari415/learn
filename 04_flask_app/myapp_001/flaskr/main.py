from flaskr import app
from flask import render_template, request, redirect, url_for
import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(BASE_DIR, "database.db")


@app.route("/")
def index():
    with sqlite3.connect(DATABASE) as con:
        db_profiles = con.execute("SELECT * FROM profile").fetchall()

    profs = [{"name": row[0], "hobby": row[1]} for row in db_profiles]
    return render_template("index.html", profs=profs)


@app.route("/result")
def result():
    return render_template("result.html")


@app.route("/register", methods=["POST"])
def register():
    name = request.form["name"]
    hobby = request.form["hobby"]

    with sqlite3.connect(DATABASE) as con:
        con.execute("INSERT INTO profile VALUES(?, ?)", [name, hobby])
        con.commit()
    return redirect(url_for("index"))
