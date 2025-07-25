# 20歳以上で、メールアドレスが gmail.com のユーザーだけを抽出
from logic.users_5 import Users


def filter_users(users, user_list):

    for user in users:
        name = user["name"]
        age = user["age"]
        email = user["email"]

        if age >= 20 and email.endswith("@gmail.com"):
            user_list[name] = email
    return user_list


def print_users(ul):
    for name, email in ul.items():
        print(f"{name} : {email}")


if __name__ == "__main__":
    users = Users.users
    ul = filter_users(users, user_list={})
    print_users(ul)
