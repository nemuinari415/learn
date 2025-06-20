# logic_010.py ファイルを読み込む
"""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
"""

from logic.logic_010 import Info_Profile

info_profile = Info_Profile()
info_profile.input_profile()
info_profile.print_profile() 

# bash
# PYTHONPATH=. python3 run/run_010.py