# logic_033.py ファイルを読み込む
from logic.logic_033 import ProductFilter

products = [
    {"name": "りんご", "category": "果物", "price": 120},
    {"name": "バナナ", "category": "果物", "price": 80},
    {"name": "にんじん", "category": "野菜", "price": 100},
    {"name": "ピーマン", "category": "野菜", "price": 90},
    {"name": "牛乳", "category": "飲料", "price": 150}
]

category = input("カテゴリーを入力 >>")

products = ProductFilter(products)
products.filter_by_category(category)
    
# bash
# PYTHONPATH=. python3 run/run_033.py