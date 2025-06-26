# logic_032.py ファイルを読み込む
from logic.logic_032 import Inquiries

inquiries = [
{"name": "田中", "category": "製品", "message": "新しいモデルについて教えて"},
{"name": "山田", "category": "サポート", "message": "動作がおかしい"},
{"name": "佐藤", "category": "製品", "message": "価格が知りたい"},
{"name": "鈴木", "category": "その他", "message": "営業電話を止めてほしい"},
{"name": "中村", "category": "サポート", "message": "Wi-Fiの接続が不安定"}
]

inquiries_obj = Inquiries(inquiries)
inquiries_obj.group_by_category()
inquiries_obj.print_category()
    
# bash
# PYTHONPATH=. python3 run/run_032.py