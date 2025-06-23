# logic_046.py ファイルを読み込む
from logic.logic_046 import HobbyClassifier

users = [
    {"name": "田中", "hobby": "読書"},
    {"name": "山田", "hobby": "読書"},
    {"name": "佐藤", "hobby": "映画"},
    {"name": "中村", "hobby": "料理"},
    {"name": "鈴木", "hobby": "料理"}
]

hc = HobbyClassifier(users)
hc.group_by_hobby() 
hc.print_summary()
    
# bash
# PYTHONPATH=. python3 run/run_046.py