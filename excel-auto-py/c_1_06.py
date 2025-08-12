from datetime import datetime, timedelta

# 基本日時を指定
base_t = datetime(2025, 2, 27)
# 3日後を計算
t = base_t + timedelta(days = 3)
# 結果を表示
print(t.strftime("%Y/%m/%d"))