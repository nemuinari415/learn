# CSVファイルの金額データを読み取り、合計を計算する
import csv

class SalesCalculator:
    def __init__(self, file_name):
        self.file_name = file_name
        self.total = 0

    def read_csv(self):
        with open(self.file_name, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader) # ヘッダーをスキップ
            self.rows = list(reader) # イテレーターをリストに保持

    def calc_total(self):
        for row in self.rows:
            try:
                self.total += int(row[1]) # 金額列
            except(IndexError, ValueError):
                print(f"不正な行をスキップ : {row}")
                
    def print_result(self):
        print(f"合計金額 : {self.total}円")        