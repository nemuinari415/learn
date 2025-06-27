# logic_011.py ファイルを読み込む
from logic.logic_011 import Phone_Books

phone_book = {
            "田中": "090-1234-5678",
            "佐藤": "080-2345-6789",
            "鈴木": "070-3456-7890"
            }

while True:
    try:
        name = input("名前を入力してください >> ")
    except:
        print("入力が間違ってます")

    if name in phone_book:
        phone_books = Phone_Books(phone_book, name)
        phone_books.print_book()
        break
    
    else:
        print("登録されていません")    

# bash
# PYTHONPATH=. python3 run/run_011.py