# p_1_33.py ファイルを読み込む
from p_1_33 import DailyLogger

memo = input("今日のメモを入力 >>")

dailylogger = DailyLogger(memo)
dailylogger.write_dialy()
dailylogger.print_dialy()