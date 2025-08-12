# 名前が3文字以上のユーザーだけを抽出して表示
from logic.users_2 import users_list

def filter_users(users, new_users):
    for user in users:
        name = user["name"]
        age = user["age"]
        
        if len(name) >= 3:
            new_users[name] = age
    return new_users

def print_users(new_users):
    for name, age in new_users.items():
        print(f"{name} : {age}")
        
def main():
    users = users_list.users
    new_users = {}
    
    filter_users(users, new_users)
    print_users(new_users)

if __name__ == "__main__":
    main()