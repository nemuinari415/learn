# logic_012.py ファイルを読み込む
from logic.logic_012 import Revers_Num_List

num_list = []
n = 1

while len(num_list) < 5:
    try:
        num_list.append(int(input(f"{n}つ目の数値を入力してください >>")))
        n += 1
    except ValueError:
        print("入力が間違ってます")

revers_num_list = Revers_Num_List(num_list)
revers_num_list.revers_num()

# bash
# PYTHONPATH=. python3 run/run_012.py