# logic_031.py ファイルを読み込む
from logic.logic_031 import ProductsPrice

products = [
    {"name": "りんご", "category": "果物", "price": 120},
    {"name": "バナナ", "category": "果物", "price": 80},
    {"name": "にんじん", "category": "野菜", "price": 100},
    {"name": "ピーマン", "category": "野菜", "price": 90},
    {"name": "牛乳", "category": "飲料", "price": 150}
]

products_price = ProductsPrice(products)
products_price.group_by_category()
products_price.output()
    
# bash
# PYTHONPATH=. python3 run/run_031.py