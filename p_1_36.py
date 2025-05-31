# p_1_35.py ファイルを読み込む
from p_1_35 import ContactManager

contact_list = {}

contact_list["名前"] = input("名前を入力 >>")
contact_list["電話"] = input("電話を入力 >>")
contact_list["メール"] = input("メールを入力 >>")

contact_manager = ContactManager(contact_list)
contact_manager.add_contact()
contact_manager.read_contacts()