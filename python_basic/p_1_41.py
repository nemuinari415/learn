# カテゴリ別の最大価格商品を表示
class MaxPriceFinder:
    def __init__(self, products):
        self.products = products
        self.mp_data = {}

    def max_price_summary(self):
        for item in self.products:
            name = item["name"]
            category = item["category"]
            price = item["price"]

            if category not in self.mp_data:
                self.mp_data[category] = [name, price]
            else:
                if price > self.mp_data[category][1]:
                    self.mp_data[category] = [name, price] 
        
    def print_max_price(self):
        print("カテゴリー : 商品名 | 価格")
        for category, (name, price) in self.mp_data.items():
            print(f"{category} : {name} | {price}円")