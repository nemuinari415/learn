# logic_017.py ファイルを読み込む
from logic.logic_017 import DailyLogger

memo = input("今日のメモを入力 >>")

dailylogger = DailyLogger(memo)
dailylogger.write_dialy()
dailylogger.print_dialy()

# bash
# PYTHONPATH=. python3 run/run_017.py