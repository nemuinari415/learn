# logic_038.py ファイルを読み込む
from logic.logic_038 import SalesManager

sales_data = [
    {"name": "りんご", "quantity": 3},
    {"name": "バナナ", "quantity": 2},
    {"name": "りんご", "quantity": 1},
    {"name": "みかん", "quantity": 5},
    {"name": "バナナ", "quantity": 4}
]

sales_manager = SalesManager(sales_data)
sales_manager.add_sales()
sales_manager.print_sales_summary()

# bash
# PYTHONPATH=. python3 run/run_038.py