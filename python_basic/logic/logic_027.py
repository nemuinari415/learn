# ファイル拡張子ごとの件数を集計するアプリ
import csv
import os
from collections import defaultdict

class ExtensionCounter:
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def scan_folder(self): # フォルダ内のファイルを取得し、拡張子ごとにカウント
        all_items = os.listdir(self.folder_path)
        self.files = [
            f for f in all_items if os.path.isfile(
                os.path.join(self.folder_path, f)
                )
            ]

    def print_summary(self): # 拡張子ごとの件数を表示
        self.counts = defaultdict(int)

        for f in self.files:
            _, ext = os.path.splitext(f)
            self.counts[ext] += 1
        
        print("拡張子 : 件数")
        for ext, count in self.counts.items():
            print(f"{ext} : {count}")


    def write_summary(self, filename): # 結果を CSV に保存（例：ext_summary.csv）
        with open(filename, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["拡張子", "件数"])
            for ext, count in self.counts.items():
                writer.writerow([ext, count])
        print("ファイルに保存しました")