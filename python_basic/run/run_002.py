# logic_002.py ファイルを読み込む
"""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
"""

from logic.logic_002 import Words_list

words = ["Python", "Programming", "Practice", "File", "Write"]

words_list = Words_list(words)
words_list.print_words()

# bash
# PYTHONPATH=. python3 run/run_002.py