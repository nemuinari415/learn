# logic_028.py ファイルを読み込む
from logic.logic_028 import SalesManagement

price_dic = {}
filename = "folder_output/" + "logic_028" + ".csv"

while True:
    price = input("商品名を入力 >>")
    try:
        price_dic[price] = int(input(f"{price}の価格を入力 >>"))
    except ValueError:
        print("入力ミスです")
        
    cont = input("入力を続けますか？[y | n] >> ")
    if cont.lower() != "y":
        break

sales_management = SalesManagement(price_dic)
sales_management.add_data()
sales_management.write_csv(filename)
sales_management.read_csv(filename)

# bash
# PYTHONPATH=. python3 run/run_028.py