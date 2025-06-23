import sqlite3
import csv

# SQLファイルを読み込む
with open('sql/s_003.sql', 'r', encoding='utf-8') as f:
    sql = f.read()

# SQLiteに接続
conn = sqlite3.connect('db/customer.db')
cur = conn.cursor()

# クエリを実行
cur.execute(sql)

# 結果を取得
rows = cur.fetchall()

# 出力
with open('sql_output/s_003.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['名前', '地区', '年齢', '合計金額', '百円単位の四捨五入'])  # ヘッダー
    writer.writerows(rows)

conn.close()