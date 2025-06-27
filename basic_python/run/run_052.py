# logic_052.py ファイルを読み込む
from logic.logic_052 import DepartmentStats

users = [
    {"name": "田中", "department": "営業", "age": 30},
    {"name": "佐藤", "department": "開発", "age": 25},
    {"name": "鈴木", "department": "営業", "age": 35},
    {"name": "山田", "department": "開発", "age": 40},
    {"name": "中村", "department": "総務", "age": 29},
]

ds = DepartmentStats(users)
ds.group_by_department()
ds.print_average_age()
