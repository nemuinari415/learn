import sqlite3

DATABASE = "flaskr/database.db"


def create_books_table():
    con = sqlite3.connect(DATABASE)
    con.execute("CREATE TABLE IF NOT EXISTS books (title, price, arrival_day)")
    con.close()
