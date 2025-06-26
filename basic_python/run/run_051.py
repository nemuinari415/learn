# logic_051.py ファイルを読み込む
from logic.logic_051 import MinPriceFinder

products = [
    {"name": "りんご", "category": "果物", "price": 120},
    {"name": "バナナ", "category": "果物", "price": 80},
    {"name": "にんじん", "category": "野菜", "price": 100},
    {"name": "ピーマン", "category": "野菜", "price": 90},
    {"name": "牛乳", "category": "飲料", "price": 150},
    {"name": "お茶", "category": "飲料", "price": 120},
]

mpf = MinPriceFinder(products)
mpf.find_min_prices()
mpf.print_summary()
