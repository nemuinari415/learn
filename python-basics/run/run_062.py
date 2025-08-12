# 年齢順にソートされたユーザーリストを返せ
def sort_users_by_age(users):
    return sorted(users, key=lambda user: user["age"])


users = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 17},
    {"name": "Charlie", "age": 30},
    {"name": "David", "age": 16},
]

suba = sort_users_by_age(users)
for user in suba:
    print(f"{user['name']} : {user["age"]}歳")
