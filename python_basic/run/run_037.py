# logic_037.py ファイルを読み込む
from logic.logic_037 import UserManager

users = []

manager = UserManager(users)
manager.add_user("田中", 28, "エンジニア")
manager.add_user("山田", 35, "デザイナー")
manager.add_user("佐藤", 22, "エンジニア")

manager.search_by_job("エンジニア")
# 出力例:
# 名前: 田中, 年齢: 28, 職業: エンジニア
# 名前: 佐藤, 年齢: 22, 職業: エンジニア

manager.search_by_job("マーケター")
# 出力例:
# 該当するユーザーはいません
    
# bash
# PYTHONPATH=. python3 run/run_037.py