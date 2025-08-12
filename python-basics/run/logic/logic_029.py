import csv

class SalesManagement:
    def __init__(self, sales_dic):
        self.sales_dic = sales_dic

    def read_add_sales(self, filename):
        with open(filename, "r", encoding="utf-8", newline="") as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                item, amount = row[0], int(row[6])
                if item in self.sales_dic:
                    self.sales_dic[item] += amount
                else:
                    self.sales_dic[item] = amount

    def print_sales(self):
        print("商品名 : 在庫")
        for item, amount in self.sales_dic.items():
            print(f"{item} : {amount}")