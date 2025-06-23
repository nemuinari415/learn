# logic_023.py ファイルを読み込む
from logic.logic_023 import ContactSearcher

filenames = "folder_sample/" + "sample_data" + ".csv"

input_names = input("名前を入力 >>")
contact_searcher = ContactSearcher(filenames, input_names)
contact_searcher.read_contacts()
contact_searcher.search_contact() 

# bash
# PYTHONPATH=. python3 run/run_023.py