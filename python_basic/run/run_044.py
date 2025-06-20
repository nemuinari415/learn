# logic_044.py ファイルを読み込む
"""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
"""

from logic.logic_044 import OutStockAnalyzer

products = [
    {"category": "食品", "name": "りんご", "stock": 0},
    {"category": "食品", "name": "バナナ", "stock": 10},
    {"category": "飲料", "name": "水", "stock": 0},
    {"category": "飲料", "name": "ジュース", "stock": 5},
    {"category": "雑貨", "name": "ティッシュ", "stock": 0}
]

o = OutStockAnalyzer(products)
o.out_stock()
o.print_stock()
    
# bash
# PYTHONPATH=. python3 run/run_044.py