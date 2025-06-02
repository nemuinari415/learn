# p_1_45.py ファイルを読み込む

from p_1_45 import ContactSearcher

filenames = "p_1_45_contacts.csv"

input_names = input("名前を入力 >>")
contact_searcher = ContactSearcher(filenames, input_names)
contact_searcher.read_contacts()
contact_searcher.search_contact() 