# logic_006.py ファイルを読み込む
from logic.logic_006 import Even_Number

numbers = [11, 22, 33, 44, 55, 66]

even_number = Even_Number(numbers)
even_number.calc_num()
even_number.print_even()

# bash
# PYTHONPATH=. python3 run/run_006.py