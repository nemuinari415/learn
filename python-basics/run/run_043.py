# logic_043.py ファイルを読み込む
from logic.logic_043 import CategoryTotalCalculator

products = [
    {"name": "りんご", "category": "果物", "price": 120},
    {"name": "みかん", "category": "果物", "price": 80},
    {"name": "キャベツ", "category": "野菜", "price": 150},
    {"name": "にんじん", "category": "野菜", "price": 100},
    {"name": "牛乳", "category": "飲料", "price": 180}
]

c = CategoryTotalCalculator(products)
c.calculate_totals()
c.print_totals()

# bash
# PYTHONPATH=. python3 run/run_043.py