# 連絡先を CSV ファイルに保存し、一覧表示するクラス
import csv
import os

class ContactManager:
    def __init__(self, contact_list):
        self.contact_list = contact_list
        self.filename = "contacts.csv"
    
    def add_contact(self):
        with open(self.filename, "a", encoding="utf-8") as f:
            for key, value in self.contact_list.items():
                  f.write(f"{key} : {value}" + "\n")
            print(f"{self.filename} に保存しました")
    
    def read_contacts(self):
        with open("contacts.csv", "r", encoding="utf-8") as f:
            content = f.read()
        print(content)