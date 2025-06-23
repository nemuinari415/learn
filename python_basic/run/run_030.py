# logic_030.py ファイルを読み込む
from logic.logic_030 import InquiriesReception
        
inquiries = [
    {"name": "田中",
        "email": "tanaka@example.com",
        "message": "資料を送ってください"},
    {"name": "山田",
        "email": "yamada@example.com",
        "message": "セミナーの開催日は？"},
    {"name": "佐藤",
        "email": "sato@example.com",
        "message": "問い合わせテストです"}
]

inquiries_reception = InquiriesReception(inquiries)
inquiries_reception.add_inquiries()

# bash
# PYTHONPATH=. python3 run/run_030.py