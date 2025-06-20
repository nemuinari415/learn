# 売上ログファイルを読み込み、商品別売上合計を出力する
import csv

class SalesAggregator:
    def __init__(self, filename): 
        self.filename = filename
        self.sales_summary = {}

    def read_data(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                next(reader)
                for row in reader:
                    if len(row) < 2:
                        continue
                    item = row[0]
                    try:
                        amount = int(row[1])
                    except ValueError:
                        continue
                    self.sales_summary[item] = self.sales_summary.get(item, 0) + amount
        except FileNotFoundError:
            print(f"ファイルが存在しません: {self.filename}")
    
    def print_summary(self): # 集計結果を商品ごとに表示
        print("[売上集計結果]")
        for item, total in self.sales_summary.items():
            print(f"{item} : {total} 円")