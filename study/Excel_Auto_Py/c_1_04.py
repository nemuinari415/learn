from datetime import datetime

# 予定日を指定
yoteibi = datetime(2026, 4, 13)
# 今日を指定
now = datetime.now()
# 日付計算
delta = yoteibi - now
#結果を表示
print("あと" + str(delta.days + 1)+"日です")