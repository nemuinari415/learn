# 複数の売上データ（商品名、数量）を渡すと、商品ごとの合計販売数を集計して表示するクラス
class SalesManager:
    def __init__(self, sales_data):
        self.sales_data = sales_data
        self.summary_data = {}
        
    def add_sales(self):
        for item in self.sales_data:
            name = item["name"]
            quantity = item["quantity"]

            if name not in self.summary_data:
                self.summary_data[name] = 0
            self.summary_data[name] += quantity

    def print_sales_summary(self):
        for name, quantity in self.summary_data.items():
            print(f"{name} : {quantity}")