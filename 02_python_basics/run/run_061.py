# 未成年のユーザー一覧を取り出せ
def get_underage_users(users, new_users):
    for user in users:
        name = user["name"]
        age = user["age"]

        if age < 20:
            new_users[name] = age
    return new_users


def print_users(new_users):
    print("未成年のユーザー")
    for name, age in new_users.items():
        print(f"{name} : {age}歳")


users = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 17},
    {"name": "Charlie", "age": 30},
    {"name": "David", "age": 16},
]

new_users: dict[str, int] = {}

get_underage_users(users, new_users)
print_users(new_users)
