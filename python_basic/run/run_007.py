# logic_007.py ファイルを読み込む
from logic.logic_007 import Dict_Marge

dict_a = {"apple": 100, "banana": 150}
dict_b = {"orange": 120, "grape": 200}

dict_marge = Dict_Marge(dict_a, dict_b)
dict_marge.marges()
dict_marge.print_marges()

# bash
# PYTHONPATH=. python3 run/run_007.py