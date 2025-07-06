from datetime import datetime

#現在時刻を取得して任意の書式で表示
t = datetime.now()
fmt = t.strftime("%Y年%m月%d日 %H時%M分%S秒")
print(fmt) # 現在時刻を文字列で表示