# カテゴリ別の在庫切れ商品一覧
class OutStockAnalyzer:
    def __init__(self, products):
        self.products = products
        self.stock_data = {}
    
    def out_stock(self):
        for item in self.products:
            category = item["category"]
            name = item["name"]
            stock = item["stock"]

            if stock == 0:
                if category not in self.stock_data:
                    self.stock_data[category] = []
                self.stock_data[category].append(name)
    
    def print_stock(self):
        print("カテゴリ別の在庫切れ商品:")
        for category, names in self.stock_data.items():
            print(f"{category}: {",".join(names)}")