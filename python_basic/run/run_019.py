# logic_019.py ファイルを読み込む
"""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
"""

from logic.logic_019 import ToDoManager

todo_manager = ToDoManager()
todo_manager.add_task()
todo_manager.show_tasks()

# bash
# PYTHONPATH=. python3 run/run_019.py