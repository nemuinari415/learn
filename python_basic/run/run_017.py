# logic_017.py ファイルを読み込む
"""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
"""

from logic.logic_017 import DailyLogger

memo = input("今日のメモを入力 >>")

dailylogger = DailyLogger(memo)
dailylogger.write_dialy()
dailylogger.print_dialy()

# bash
# PYTHONPATH=. python3 run/run_017.py