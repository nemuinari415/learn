# logic_015.py ファイルを読み込む
from logic.logic_015 import WeekDay

weekday_jp = ["月", "火", "水", "木", "金", "土", "日"]

while True:
    day = input("日付を入力(2025-05-29) >>")
    try:
        weekday = WeekDay(day, weekday_jp)
        weekday.d_times()
        weekday.print_weekday()
        break
    except ValueError:
        print("入力が間違ってます")

# bash
# PYTHONPATH=. python3 run/run_015.py