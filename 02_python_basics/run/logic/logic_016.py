# ログ保存アプリ（ミニ日誌）
from datetime import date

class DiaryLogger:
    def __init__(self, diary):
        self.diary = diary
        self.todays = date.today().isoformat()
    
    def write_diary(self):
        with open("folder_output/logic_016.txt", "a", encoding="utf-8", newline="") as f:
            f.write(f"{self.todays} : {self.diary}" + "\n" )
    
    def print_diary(self):
        print(f"{self.todays} : {self.diary}")