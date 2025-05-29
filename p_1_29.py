# 日付を入力して、曜日を表示する関数
from datetime import datetime

class WeekDay:
    def __init__(self, day, weekday_jp):
        self.day = day
        self.weekday_jp = weekday_jp
    
    def d_times(self):
        self.day_obj = datetime.strptime(self.day, "%Y-%m-%d")
        self.week_obj = self.weekday_jp[self.day_obj.weekday()]

    def print_weekday(self):
        print(f"{self.day_obj.strftime("%Y年%m月%d日")}は、{self.week_obj}曜日です。")