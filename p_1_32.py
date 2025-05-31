# p_1_31.py ファイルを読み込む
from p_1_31 import DiaryLogger

diary = input("今日の出来事（１行）を入力 >>")

diary_today = DiaryLogger(diary)
diary_today.write_diary()
diary_today.print_diary()