# カテゴリ別に商品を整理して表示する（辞書とリストの応用）
class ProductsPrice:
    def __init__(self, products):
        self.products = products
        self.category_map = {}

    def group_by_category(self):
        for p in self.products:
            name, category, price = p["name"], p["category"], p["price"]
            if category not in self.category_map:
                self.category_map[category] = []
            self.category_map[category].append((name, price))
           
    def output(self):
        for category, items in self.category_map.items():
            print(f"--- {category} ---")
            for name, price in items:
                print(f"{name} : {price}円")
            print()