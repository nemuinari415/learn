# Requests モジュールを取り込む
import requests

# 現在時刻を提供しているサーバーにアクセス
url = "https://api.aoikujira.com/time/get.php"
result = requests.get(url)

#結果を表示
print(result.text)