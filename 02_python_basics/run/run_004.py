# logic_004.py ファイルを読み込む
from logic.logic_004 import Min_Max

numbers = [13, 7, 20, 3, 19, 2, 8]

min_max = Min_Max(numbers)
min_max.min_max_calc()
min_max.print_num()

# bash
# PYTHONPATH=. python3 run/run_004.py