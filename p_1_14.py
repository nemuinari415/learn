# #p_1_13.py ファイルを読み込む
from p_1_13 import Dict_Marge

dict_a = {"apple": 100, "banana": 150}
dict_b = {"orange": 120, "grape": 200}

dict_marge = Dict_Marge(dict_a, dict_b)
dict_marge.marges()
dict_marge.print_marges()