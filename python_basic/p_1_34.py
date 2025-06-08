# カテゴリごとの商品の平均価格を計算するクラスを作成
class ProductStats:
    def __init__(self, products):
        self.products = products
        self.category_dict = {}  # 例：{"果物": [200, 2]}

    def group_by_category(self):
        for item in self.products:
            category = item["category"]
            price = item["price"]
            if category not in self.category_dict:
                self.category_dict[category] = [0, 0]  # [合計金額, 件数]
            self.category_dict[category][0] += price
            self.category_dict[category][1] += 1

    def print_average_price(self):
        for category, (total, count) in self.category_dict.items():
            avg = total / count
            print(f"{category} の平均価格は {round(avg)} 円です")