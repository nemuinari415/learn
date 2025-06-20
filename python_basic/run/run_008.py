# logic_008.py ファイルを読み込む
"""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
"""

from logic.logic_008 import Palindrome

palindrome = Palindrome()
palindrome.input_word()
palindrome.is_palindrome()
palindrome.print_p()

# bash
# PYTHONPATH=. python3 run/run_008.py