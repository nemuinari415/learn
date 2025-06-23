import sqlite3
import csv

# SQLファイルを読み込む
with open('sql/s_001.sql', 'r', encoding='utf-8') as f:
    sql = f.read()

# SQLiteに接続
conn = sqlite3.connect('db/school.db')
cur = conn.cursor()

# クエリを実行
cur.execute(sql)

# 結果を取得
rows = cur.fetchall()

# 出力
with open('sql_output/s_001.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['student_name', 'course_name'])  # ヘッダー
    writer.writerows(rows)

conn.close()