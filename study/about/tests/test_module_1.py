from src.module_1 import all_books
import sqlite3
import pytest


@pytest.fixture
def db_con():
    con = sqlite3.connect("local_database.db")
    print("before yield")
    yield con
    print("after yield")
    con.close()


def test_all_books_1(db_con):
    books = all_books(db_con)
    assert books == []
