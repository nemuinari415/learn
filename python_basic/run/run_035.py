# logic_035.py ファイルを読み込む
"""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
"""

from logic.logic_035 import ProductFilter

products = [
    {"name": "りんご", "price": 120},
    {"name": "バナナ", "price": 80},
    {"name": "牛乳", "price": 150},
    {"name": "コーヒー", "price": 200}
]

filter_obj = ProductFilter(products)
filter_obj.filter_by_min_price(150)
    
# bash
# PYTHONPATH=. python3 run/run_035.py