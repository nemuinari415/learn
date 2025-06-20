import csv

class SalesAnalyzer:
    def __init__(self, filename):
        self.filename = filename
        self.sales_dic = {}
        self.total = 0
    
    def read_csv_data(self):
        with open(self.filename, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                if len(row) < 7:
                    print(f"列数不足の行をスキップ: {row}")
                    continue
                try:
                    item = row[0]
                    price = int(row[1])
                    days = row[2]
                    quantity = int(row[6])
                except ValueError:
                    print(f"不正な数値データをスキップ: {row}")
                    continue

                if item in self.sales_dic:
                    old_days, old_price, old_quantity = self.sales_dic[item]
                    self.sales_dic[item] = (days, price, old_quantity + quantity)   
                else:
                    self.sales_dic[item] = (days, price, quantity)
    
    def calculate_total_sales(self):
        self.total = 0
        for item, (days, price, quantity) in self.sales_dic.items():
            self.total += price * quantity

        self.sales_dic = dict(sorted(
            self.sales_dic.items(),
            key=lambda x: x[1][1] * x[1][2],  # price * quantity
            reverse=True
        ))

    def print_csv_data(self):
        for item, (days, price, quantity) in self.sales_dic.items():
            print(f"日付 : {days} | 商品名 : {item} | 値段 : {price}円 | 数量 : {quantity}個")
        print(f"合計金額 : {self.total}円")