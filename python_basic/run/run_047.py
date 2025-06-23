# logic_047.py ファイルを読み込む
"""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
"""

from logic.logic_047 import StaffSalesSummary

read_filename = "folder_sample/" + "sample_data" + ".csv"
write_filename = "folder_output/" + "logic_047" + ".csv"

sss = StaffSalesSummary(read_filename, write_filename)
sss.read_csv()
sss.write_csv()
    
# bash
# PYTHONPATH=. python3 run/run_047.py