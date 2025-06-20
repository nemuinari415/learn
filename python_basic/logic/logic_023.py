# 連絡帳アプリ（名前で検索)
import csv
class ContactSearcher:
    def __init__(self, filenames, input_names):
        self.filenames = filenames
        self.input_names = input_names
        self.contact_dict = {}

    def read_contacts(self):
        with open(self.filenames, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                name, tel, mail = row[3], row[4], row[5]
                self.contact_dict[name] = tel, mail

    def search_contact(self):
        self.input_names = self.input_names.strip()
        # 名前の前後に空白が入ってると一致しない対策
        if self.input_names in self.contact_dict:
            tel, mail = self.contact_dict[self.input_names]
            print(f"名前 : {self.input_names}")
            print(f"電話番号 : {tel}")
            print(f"メール : {mail}")
        else:
            print("該当する連絡先は見つかりませんでした。")