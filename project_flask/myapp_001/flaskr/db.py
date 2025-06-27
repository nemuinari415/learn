import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(BASE_DIR, "database.db")


def create_profile_table():
    with sqlite3.connect(DATABASE) as con:
        con.execute("CREATE TABLE IF NOT EXISTS profile (name TEXT, hobby TEXT)")
        con.commit()
