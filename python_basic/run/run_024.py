# logic_024.py ファイルを読み込む
"""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
"""

from logic.logic_024 import SalesAnalyzer

filenames = "folder_sample/" + "sample_data" + ".csv"

sales_analyzer = SalesAnalyzer(filenames)
sales_analyzer.read_csv_data()
sales_analyzer.calculate_total_sales()
sales_analyzer.print_csv_data()

# bash
# PYTHONPATH=. python3 run/run_024.py