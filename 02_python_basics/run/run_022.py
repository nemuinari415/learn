# logic_022.py ファイルを読み込む
from logic.logic_022 import SalesAggregator

filename = "folder_sample/" + "sample_data" + ".csv"

s = SalesAggregator(filename)
s.read_data()
s.print_summary()

# bash
# PYTHONPATH=. python3 run/run_022.py