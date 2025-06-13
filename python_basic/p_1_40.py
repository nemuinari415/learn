# 年齢別ユーザー分類
class UserAgeClassifier:
    def __init__(self, users):
        self.users = users
        self.classify_data = {}

    def classify_by_age(self):
        for item in self.users:
            name = item["name"]
            age = item["age"]

            if age <= 19:
                category = "ages1"
            
            elif age >= 20 and age <= 39:
                category = "ages2"

            else:
                category = "ages3"

            if category not in self.classify_data:
                self.classify_data[category] = []
                        
            self.classify_data[category].append(name)

    def print_summary(self):
        for category, names in self.classify_data.items():
            if category == "ages1":
                print(f"10代以下 : [{', '.join(names)}]")
            if category == "ages2":
                print(f"20~30代 : [{', '.join(names)}]")
            if category == "ages3":
                print(f"40代以上 : [{', '.join(names)}]")