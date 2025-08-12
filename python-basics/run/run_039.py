# logic_039.py ファイルを読み込む
from logic.logic_039 import InquiryManager

inquiries = [
    {"name": "田中", "category": "製品", "message": "新モデルについて教えて"},
    {"name": "山田", "category": "サポート", "message": "使い方が分かりません"},
    {"name": "佐藤", "category": "製品", "message": "価格を教えて"},
    {"name": "鈴木", "category": "その他", "message": "営業電話は不要です"}
]

inquiry_obj = InquiryManager(inquiries)
inquiry_obj.count_by_category()
inquiry_obj.print_summary()

# bash
# PYTHONPATH=. python3 run/run_039.py