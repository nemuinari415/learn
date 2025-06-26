# 指定フォルダ内のファイル一覧を取得し、CSV に保存するアプリ
import csv
import os

class FolderScanner:
    def __init__(self, folder_path):
        self.folder_path = folder_path
    
    def scan_files(self): # 対象フォルダ内のファイルをスキャン
        all_items = os.listdir(self.folder_path)
        #フォルダ内のファイル一覧を取得
        
        self.files = [
            f for f in all_items if os.path.isfile(
                os.path.join(self.folder_path, f)
                )
            ]
        # 「all_items に含まれる要素 f のうち
        # ファイルであるものだけを self.files にリストで格納する」

    def save_to_csv(self, filename): # ファイル情報をCSVに保存
        with open(filename, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["ファイル名","拡張子"]) # ヘッダー
            for f in self.files:
                name, ext = os.path.splitext(f) # 拡張子を分離
                writer.writerow([name, ext])
        print("ファイルが出力されました。")
    
    def print_summary(self, filename): # 取得したファイル件数と内容を表示
        with open(filename, "r", encoding="utf-8", newline="") as f:
            reader = csv.reader(f)
            for row in reader:
                print(",".join(row))