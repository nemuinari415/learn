# logic_003.py ファイルを読み込む
"""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
"""

from logic.logic_003 import Rectangle

r = Rectangle()
r.input_v()
r.area()
r.print_v()

# bash
# PYTHONPATH=. python3 run/run_003.py