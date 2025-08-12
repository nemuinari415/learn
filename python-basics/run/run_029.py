# logic_029.py ファイルを読み込む
from logic.logic_029 import SalesManagement

filename = "folder_sample/sample_data.csv"
sales_dic = {}

sales_management = SalesManagement(sales_dic)
sales_management.read_add_sales(filename)
sales_management.print_sales()

# bash
# PYTHONPATH=. python3 run/run_029.py