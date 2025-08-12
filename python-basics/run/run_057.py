# メールアドレスのバリデーション関数
def is_valid_email(email):
    if len(email) < 8:
        print("メールアドレスは8文字以上である必要があります。")
        return

    if email.count("@") != 1:
        print("「@」が1つだけ含まれている必要があります。")
        return

    if email.startswith("@") or email.endswith("@"):
        print("「@」が先頭や末尾にあってはいけません。")
        return

    if email.startswith(".") or email.endswith("."):
        print("「.」が先頭や末尾にあってはいけません。")
        return

    # 分割してドメイン部分のドット確認
    local, domain = email.split("@")
    if "." not in domain:
        print("ドメイン部に「.」が必要です（例：example.com）")
        return

    # すべての条件をクリア
    print(f"「{email}」は有効なメールアドレスです。登録されました。")


# 実行部分
email = input("メールアドレス >> ")
is_valid_email(email)
