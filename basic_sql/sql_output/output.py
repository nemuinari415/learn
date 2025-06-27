import sqlite3
import csv

# SQLファイルを読み込む
with open("sql/s_009.sql", "r", encoding="utf-8") as f:
    sql = f.read()

# SQLiteに接続
conn = sqlite3.connect("db/customer.db")
cur = conn.cursor()

# クエリを実行
cur.execute(sql)

# 結果を取得
rows = cur.fetchall()

# 出力
with open("sql_output/s_009.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["商品名", "在庫数", "注文数", "超過数"])  # ヘッダー
    writer.writerows(rows)

conn.close()
