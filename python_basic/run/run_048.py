# logic_048.py ファイルを読み込む
from logic.logic_048 import LogAnalyzer

logs = [
    {"user": "田中", "action": "ログイン"},
    {"user": "山田", "action": "ログイン"},
    {"user": "田中", "action": "データ閲覧"},
    {"user": "佐藤", "action": "ログアウト"},
    {"user": "山田", "action": "データ編集"},
    {"user": "田中", "action": "ログアウト"},
    {"user": "山田", "action": "ログアウト"},
]

la = LogAnalyzer(logs)
la.logs_totalling()
la.print_totalling()
    
# bash
# PYTHONPATH=. python3 run/run_048.py