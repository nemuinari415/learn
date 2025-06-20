# logic_040.py ファイルを読み込む
"""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
"""

from logic.logic_040 import UserAgeClassifier

users = [
    {"name": "田中", "age": 18},
    {"name": "佐藤", "age": 25},
    {"name": "中村", "age": 34},
    {"name": "鈴木", "age": 45}
]

u = UserAgeClassifier(users)
u.classify_by_age()
u.print_summary()

# bash
# PYTHONPATH=. python3 run/run_040.py