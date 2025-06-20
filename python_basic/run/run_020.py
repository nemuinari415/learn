# logic_020.py ファイルを読み込む
"""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
"""

from logic.logic_020 import SalesCalculator

file_name = "folder_sample/" + "sample_data" + ".csv"

sales_calculator = SalesCalculator(file_name)
sales_calculator.read_csv()
sales_calculator.calc_total()
sales_calculator.print_result()

# bash
# PYTHONPATH=. python3 run/run_020.py