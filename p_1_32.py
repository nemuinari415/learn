class Inquiries:
    def __init__(self, inquiries):
        self.inquiries = inquiries
        self.category_count = {}

    def group_by_category(self):
        for i in self.inquiries:
            category = i["category"]
            if category not in self.category_count:
                self.category_count[category] = 0
            self.category_count[category] += 1

    def print_category(self):
        print("カテゴリ別件数:")
        for category, count in self.category_count.items():
            print(f"{category} : {count} 件")