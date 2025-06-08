# 特定のカテゴリーの商品だけを表示する
class ProductFilter:
    def __init__(self, products):
        self.products = products

    def filter_by_category(self, category):
        print(f"カテゴリ : {category}")
        found = False # 一致する商品があったかどうかを記録

        for item in self.products:
            if item["category"] == category:
                print(f"{item['name']} - {item['price']}")
                found = True
            
        if not found: # False なら...
            print("在庫がありませんでした")