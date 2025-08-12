# 20歳以上30歳以下のユーザーだけを抽出して表示する関数
from logic.users_1 import Users

def filter_users_by_age(users):
    for u in users:
        if 20 <= u["age"] <= 30:
            print(f"{u['name']} : {u['age']}歳")

def main():
    users = Users.users
    filter_users_by_age(users)
    
if __name__ == "__main__":
    main()