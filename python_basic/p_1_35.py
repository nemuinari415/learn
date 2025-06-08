# 特定価格以上の商品だけを抽出
class ProductFilter:
    def __init__(self, products):
        self.products = products

    def filter_by_min_price(self, min_price):
        hit = False
        for item in self.products:
            name = item["name"]
            price = item["price"]
            if price >= min_price:
                print(f"{name} - {price}")
                hit = True
        if not hit:
            print("該当する商品はありません")