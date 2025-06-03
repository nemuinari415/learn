# 売上ログファイルを読み込み、商品別売上合計を出力する
import csv

class SalesAggregator:
    def __init__(self, filenames):
        self.filenames = filenames
        self.sales_summary = {}

    def read_data(self): # CSVファイルを読み込み、商品ごとの合計を集計
        with open(self.filenames, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader) # ヘッダーをスキップ
            for row in reader:
                item, amount = row[0], int(row[1]) 
                # item = "商品名", amount = 値段
                if item in self.sales_summary:
                    self.sales_summary[item] += amount
                else:
                    self.sales_summary[item] = amount
    
    def print_summary(self): # 集計結果を商品ごとに表示
        print("[売上集計結果]")
        for item, total in self.sales_summary.items():
            print(f"{item} : {total} 円")