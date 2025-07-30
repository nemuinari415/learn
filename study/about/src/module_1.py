def add_numbers(a, b):
    return a + b


def all_books(con):
    books = con.execute("SELECT * FROM books").fetchall()
    return books
