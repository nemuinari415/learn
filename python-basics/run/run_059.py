# ユーザー情報のリストから特定条件のユーザーを抽出せよ
"""
上記の users から、20歳以上のユーザーだけを抽出し、名前だけをリストにして出力する関数
get_adult_usernames(users: list) を作成してください。
"""


def get_adult_usernames(users):
    for user in users:
        name = user["name"]
        age = user["age"]
        if age >= 20:
            print(f"{name}: {age}歳")


users = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 17},
    {"name": "Charlie", "age": 30},
    {"name": "David", "age": 16},
]

get_adult_usernames(users)
