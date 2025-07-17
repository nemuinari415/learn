# 名前を入力すると、そのユーザーの情報（年齢）を表示する関数
def find_user_age(users):

    i_name = input("名前を入力してください >>")

    for user in users:
        name = user["name"]
        age = user["age"]

        if name.lower() == i_name.lower():
            print(f"{name}さんは、{age}歳です")
            return
    print("そのユーザーはいません")


users = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 17},
    {"name": "Charlie", "age": 30},
    {"name": "David", "age": 16},
]

find_user_age(users)
