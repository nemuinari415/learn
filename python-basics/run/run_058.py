# ユーザー名のバリデーション関数
import string

symbols = string.punctuation  # 記号


def is_valid_username(username):

    # 5文字以下なら
    if len(username) < 5:
        print("5文字以上で入力してください。")
        return

    # 半角英数字か？
    if not username.isalnum():
        print("半角英数字で入力してください")
        return

    # 記号が含まれるなら
    if any(c in symbols for c in username):
        print("記号を含めないでください。")
        return

    # 数字が含まれるか？
    if not any(c.isdigit() for c in username):
        print("数字を含めてください。")
        return

    # 英字が１文字以上含まれるか？
    if not any(c.isalpha() for c in username):
        print("文字を入れてください")
        return

    print(f"登録ユーザーネーム:{username}")


username = input("UserName >> ")
is_valid_username(username)
