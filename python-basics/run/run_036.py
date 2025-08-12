# logic_036.py ファイルを読み込む
from logic.logic_036 import PriceBandClassifier

products = [
    {"name": "りんご", "price": 120},
    {"name": "バナナ", "price": 80},
    {"name": "牛乳", "price": 150},
    {"name": "コーヒー", "price": 200},
    {"name": "お菓子", "price": 90}
]

price_Band_classifier = PriceBandClassifier(products)
price_Band_classifier.classify_by_price_band()
price_Band_classifier.print_cbpb_data()
    
# bash
# PYTHONPATH=. python3 run/run_036.py