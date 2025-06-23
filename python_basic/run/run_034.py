# logic_034.py ファイルを読み込む
from logic.logic_034 import ProductStats

products = [
    {"name": "りんご", "category": "果物", "price": 120},
    {"name": "バナナ", "category": "果物", "price": 80},
    {"name": "にんじん", "category": "野菜", "price": 100},
    {"name": "ピーマン", "category": "野菜", "price": 90},
    {"name": "牛乳", "category": "飲料", "price": 150},
    {"name": "コーヒー", "category": "飲料", "price": 200}
]

products_stats = ProductStats(products)
products_stats.group_by_category()
products_stats.print_average_price()
    
# bash
# PYTHONPATH=. python3 run/run_034.py