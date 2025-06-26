import sqlite3
import csv

# SQLファイルを読み込む
with open('sql/s_008.sql', 'r', encoding='utf-8') as f:
    sql = f.read()

# SQLiteに接続
conn = sqlite3.connect('db/customer.db')
cur = conn.cursor()

# クエリを実行
cur.execute(sql)

# 結果を取得
rows = cur.fetchall()

# 出力
with open('sql_output/s_008.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['ID', '顧客名', '商品名', '注文数'])  # ヘッダー
    writer.writerows(rows)

conn.close()