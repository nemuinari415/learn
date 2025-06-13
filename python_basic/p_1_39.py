# お問い合わせデータをカテゴリ別に集計して、件数を表示する
class InquiryManager:
    def __init__(self, inquiries):
        self.inquiries = inquiries
        self.category_data = {}

    def count_by_category(self): # 各カテゴリごとの件数を集計
        for item in self.inquiries:
            category = item["category"]
            message = item["message"]

            if category not in self.category_data:
                self.category_data[category] = []
            self.category_data[category].append(message)

    def print_summary(self):
        print("カテゴリ別のお問い合わせ件数:")
        for category, count in self.category_data.items():
            print(f"{category} : {len(count)}件")