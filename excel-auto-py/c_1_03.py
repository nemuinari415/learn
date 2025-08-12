from datetime import datetime
# 2022/01/01を指定してオブジェクトを作成
t = datetime(2022, 1, 1)
# 日付を表示
print(t.strftime("%Y年%m月%d日")) # 結果例：2022年01月01日