# 簡易売上管理ツール
import csv

class SalesManagement:
    def __init__(self, price_dic):
        self.price_dic = price_dic
        self.total = 0
    
    def add_data(self): # 合計金額と平均金額を計算
        for price, amount in self.price_dic.items():
            self.total += amount
        
        self.avg = self.total / len(self.price_dic)
        print("[計算結果]")
        print(f"合計 : {self.total}円")
        print(f"平均 : {self.avg:.1f}円")
    
    def write_csv(self, filename):
        with open(filename, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["商品名", "金額"])
            for price, amount in self.price_dic.items():
                writer.writerow([price, amount])
        print("ファイルに保存しました")
    
    def read_csv(self, filename):
        with open(filename, "r", encoding="utf-8", newline="") as f:
            reader = csv.reader(f)
            next(reader)
            print("[ファイルの内容]")
            for row in reader:
                item, amount = row[0], int(row[1])
                print(f"{item} : {amount}")