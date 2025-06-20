# logic_009.py ファイルを読み込む
"""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
"""

from logic.logic_009 import Data_list

data = [1, 3, 5, 7]

data_list = Data_list(data)
data_list.map_lambda()
data_list.print_data()

# bash
# PYTHONPATH=. python3 run/run_009.py