# パスワードの安全性をチェック関数を作成
import string

symbols = string.punctuation  # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

print("※８文字以上、英大文字を１つ以上含む")
print("※英小文字を１つ以上含む、数字を１つ以上含む")
print("（!@#$%^&*()-_+= など）を１つ以上含む")

password = input("パスワードを入力してください >> ")


def check_password_strength(password):
    # パスワード長さチェック
    if len(password) < 8:
        print("パスワードは8文字以上である必要があります。")
        return

    has_upper = False  # 大文字判定
    has_lower = False  # 小文字判定
    has_digit = False  # 数字判定
    has_symbol = False  # 記号判定

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in symbols:
            has_symbol = True

    if has_upper and has_lower and has_digit and has_symbol:
        print(f"password : {password}")
        print("登録されました。")
    else:
        print("入力に誤りがあります。以下を確認してください：")
        if not has_upper:
            print("- 大文字を含めてください")
        if not has_lower:
            print("- 小文字を含めてください")
        if not has_digit:
            print("- 数字を含めてください")
        if not has_symbol:
            print("- 記号（!@#など）を含めてください")


check_password_strength(password)
