# dataclases の活用
from dataclasses import dataclass
from logic.users_5 import Users


@dataclass
class User:
    name: str
    age: int
    email: str


def input_data(users):
    new_users = []

    for user in users:
        if user["age"] >= 18:
            new_users.append(
                User(name=user["name"], age=user["age"], email=user["email"])
            )
    return new_users


def print_data(new_users):
    for user in new_users:
        print(
            f"名前: {user.name}, 年齢: {user.age}, メールアドレス: {user.email}"
        )


if __name__ == "__main__":
    users = Users.users
    new_users = input_data(users)
    print_data(new_users)
