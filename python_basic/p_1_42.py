# カテゴリごとの在庫数と平均価格を表示するクラスを作成しよう
class StockAnalyzer:
    def __init__(self, products):
        self.products = products
        self.group_data = {}
    
    def group_by_category(self):
        for item in self.products:
            name = item["name"]
            category = item["category"]
            price = item["price"]
            stock = item["stock"]

            if category not in self.group_data:
                self.group_data[category] = [0, 0, 0] # 合計金額、総在庫数、商品数
            self.group_data[category][0] += price
            self.group_data[category][1] += stock
            self.group_data[category][2] += 1
    
    def print_summary(self):
        for category, (price, stock, count) in self.group_data.items():
            avg = price / count
            print(f"{category} - 在庫: {stock}個 | 平均価格: {round(avg)}円")