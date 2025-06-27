# logic_041.py ファイルを読み込む
from logic.logic_041 import MaxPriceFinder

products = [
    {"name": "りんご", "category": "果物", "price": 120},
    {"name": "バナナ", "category": "果物", "price": 80},
    {"name": "にんじん", "category": "野菜", "price": 100},
    {"name": "ピーマン", "category": "野菜", "price": 90},
    {"name": "牛乳", "category": "飲料", "price": 150}
]

m = MaxPriceFinder(products)
m.max_price_summary()
m.print_max_price() 

# bash
# PYTHONPATH=. python3 run/run_041.py