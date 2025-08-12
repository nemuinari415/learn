# カテゴリ別の最安値商品を表示する
class MinPriceFinder:
    def __init__(self, products):
        self.products = products
        self.min_data = {}

    def find_min_prices(self):
        for item in self.products:
            name = item["name"]
            category = item["category"]
            price = item["price"]

            if category not in self.min_data:
                self.min_data[category] = [name, price]
            if self.min_data[category][1] > price:
                self.min_data[category] = [name, price]

    def print_summary(self):
        print("カテゴリー ： 商品名(値段)")
        for category, (names, min_price) in self.min_data.items():
            name = names
            price = min_price
            print(f"{category} : {name} ({price}円)")
