# ユーザー情報の登録と検索
class UserManager:
    def __init__(self, users):
        # ユーザー情報を保持（リスト）
        self.users = users
        self.user_data = {}

    def add_user(self, name, age, job):
        # 1人分のユーザー情報を追加する（辞書で）
        if job not in self.user_data:
            self.user_data[job] = []
        self.user_data[job].append({"name": name, "age": age})

    def search_by_job(self, job):
        # 指定された職業のユーザーのみ表示する
        if job in self.user_data:
            for user in self.user_data[job]:
                print(f"名前: {user['name']}, 年齢: {user['age']}歳, 職業: {job}")

        # 見つからなければ「該当するユーザーはいません」と表示
        else:
            print(f"該当するユーザーはいません({job})")