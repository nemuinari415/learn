# logic_045.py ファイルを読み込む
from logic.logic_045 import LoginTracker

logs = [
    {"user": "田中", "time": "morning"},
    {"user": "山田", "time": "afternoon"},
    {"user": "佐藤", "time": "afternoon"},
    {"user": "中村", "time": "night"},
    {"user": "鈴木", "time": "morning"},
    {"user": "伊藤", "time": "afternoon"}
]

lt = LoginTracker(logs)
lt.group_by_time()
lt.print_summary()
    
# bash
# PYTHONPATH=. python3 run/run_045.py