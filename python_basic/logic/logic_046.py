# 趣味別のユーザー一覧を作成する
class HobbyClassifier:
    def __init__(self, users):
        self.users = users
        self.hobby_data = {}

    def group_by_hobby(self):
        for item in self.users:
            name = item["name"]
            hobby = item["hobby"]

            if hobby not in self.hobby_data:
                self.hobby_data[hobby] = []
            self.hobby_data[hobby].append(name)

    def print_summary(self):
        print("趣味別ユーザー一覧")
        for hobby, names in self.hobby_data.items():
            print(f"{hobby} : {",".join(names)}")