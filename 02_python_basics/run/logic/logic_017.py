# ログを日別ファイルに記録するクラス
from datetime import date

class DailyLogger:
    def __init__(self, memo):
        self.memo = memo

    def write_dialy(self):
        self.filename = "folder_output/" + "logic_017_" + date.today().isoformat() + ".txt"
        with open(self.filename, "a", encoding="utf-8") as f:
            f.write(self.memo + "\n")
        
    def print_dialy(self):
        print(f"書き込み完了 : {self.filename} に記録しました")
        print(f"内容 : {self.memo}")