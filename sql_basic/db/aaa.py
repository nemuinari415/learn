import pandas as pd
import sqlite3

# 全シートを辞書で取得
sheets = pd.read_excel("sample_data.xlsx", sheet_name=None)

# SQLite DBに接続
conn = sqlite3.connect("customer.db")

# シート名ごとにテーブルを作成して保存
for sheet_name, df in sheets.items():
    df.to_sql(sheet_name, conn, if_exists="replace", index=False)
    print(f"{sheet_name} を取り込みました")

# 確認（例として最初のシートの内容を表示）
first_sheet = list(sheets.keys())[0]
print(pd.read_sql(f"SELECT * FROM '{first_sheet}'", conn))

conn.close()