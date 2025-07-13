# 名前でユーザーを検索せよ
def find_user_by_name(users, input_name):
    for u in users:
        name = u["name"]
        age = u["age"]
        if input_name.lower() == name.lower():  # 大文字小文字無視
            print(f"{name} : {age}")
            return
    print("ユーザーが見つかりませんでした")


users = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 17},
    {"name": "Charlie", "age": 30},
    {"name": "David", "age": 16},
]

input_name = input("検索する名前を入力してください >>")
find_user_by_name(users, input_name)
