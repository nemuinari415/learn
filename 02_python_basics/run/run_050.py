# logic_050.py ファイルを読み込む
from logic.logic_050 import PurchaseHistory

logs = [
    {"user": "田中", "item": "りんご", "price": 120},
    {"user": "田中", "item": "バナナ", "price": 100},
    {"user": "山田", "item": "りんご", "price": 120},
    {"user": "田中", "item": "りんご", "price": 120},
    {"user": "佐藤", "item": "バナナ", "price": 100},
    {"user": "山田", "item": "みかん", "price": 80},
]

ph = PurchaseHistory(logs)
ph.add_logs()
ph.print_summary()
