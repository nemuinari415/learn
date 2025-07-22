# 正しい形式のメールアドレスを持つユーザーだけを抽出して表示する関数
from logic.users_3 import Users

true_users = {}


def true_address(users, true_users):
    for user in users:
        name = user["name"]
        email = user["email"]

        if "@" in email and "." in email:
            if email.count("@") == 1 and email.count(".") >= 1:
                true_users[name] = email

    return true_users


def print_users(true_users):
    for name, email in true_users.items():
        print(f"Name: {name}, Email: {email}")


if __name__ == "__main__":
    users = Users.users
    true_users = true_address(users, true_users)
    print_users(true_users)
