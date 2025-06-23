# logic_042.py ファイルを読み込む
from logic.logic_042 import StockAnalyzer

products = [
    {"name": "りんご", "category": "果物", "price": 120, "stock": 5},
    {"name": "バナナ", "category": "果物", "price": 80, "stock": 8},
    {"name": "にんじん", "category": "野菜", "price": 100, "stock": 6},
    {"name": "ピーマン", "category": "野菜", "price": 90, "stock": 7},
    {"name": "牛乳", "category": "飲料", "price": 150, "stock": 10}
]

s = StockAnalyzer(products)
s.group_by_category()
s.print_summary()

# bash
# PYTHONPATH=. python3 run/run_042.py