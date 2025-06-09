# 価格帯で商品を分類する
class PriceBandClassifier:
    def __init__(self, products):
        self.products = products
        self.cbpb_data = {}
    
    def classify_by_price_band(self):
        for item in self.products:
            price = item["price"]
            name = item["name"]

            if price <= 99:
                category = "低価格帯"
        
            elif price >= 100 and price <= 199:
                category = "中価格帯"
        
            elif price >= 200:
                category = "高価格帯"
        
            # category リストの初期化（重要）
            if category not in self.cbpb_data:
                self.cbpb_data[category] = []   
            self.cbpb_data[category].append(name)
    
    def print_cbpb_data(self):
        for category, names in self.cbpb_data.items():
            print(f"{category} : {','.join(names)}")