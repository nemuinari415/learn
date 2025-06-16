# カテゴリごとの合計価格を集計
class CategoryTotalCalculator:
    def __init__(self, products):
        self.products = products
        self.total_data = {}
        
    def calculate_totals(self):
        for item in self.products:
            name = item["name"]
            category = item["category"]
            price = item["price"]

            if category not in self.total_data:
                self.total_data[category] = 0
            self.total_data[category] += price

    def print_totals(self):
        for category, total in self.total_data.items():
            print(f"{category} : {total}円")