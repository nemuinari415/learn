# 連絡先を CSV ファイルに保存し、一覧表示するクラス
import csv
import os

class ContactManager:
    def __init__(self, contact_list):
        self.contact_list = contact_list
        self.filename = "folder_output/" + "logic_018" + ".csv"
    
    def add_contact(self):
        is_new = not os.path.exists(self.filename)
        with open(self.filename, "a", encoding="utf-8") as f:
            writer = csv.writer(f)
            if is_new:
                writer.writerow(self.contact_list.keys()) # ヘッダー
            writer.writerow(self.contact_list.values())
        print(f"{self.filename} に保存しました")
    
    def read_contacts(self):
        with open(self.filename, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                print(" | ".join(row))