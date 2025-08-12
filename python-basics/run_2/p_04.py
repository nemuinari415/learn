"""
メールアドレスのドメイン（@以降）が gmail.com のユーザーだけを抽出し、名前とメールを表示する 関数
"""

from logic.users_4 import Users


def filter_gmail_users(users, gmail_users):

    for user in users:
        name = user["name"]
        email = user["email"]

        if email.endswith("@gmail.com"):
            gmail_users[name] = email

    return gmail_users


def print_gmail_users(gmail_users):
    for name, email in gmail_users.items():
        print(f"{name} : {email}")


if __name__ == "__main__":

    gmail_users = {}

    users = Users.users
    filter_gmail_users(users, gmail_users)
    print_gmail_users(gmail_users)
