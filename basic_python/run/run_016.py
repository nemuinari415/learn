# logic_016.py ファイルを読み込む
from logic.logic_016 import DiaryLogger

diary = input("今日の出来事（１行）を入力 >>")

diary_today = DiaryLogger(diary)
diary_today.write_diary()
diary_today.print_diary()

# bash
# PYTHONPATH=. python3 run/run_016.py