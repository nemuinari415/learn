import openpyxl as excel

# 新規ワークブックを作る
book = excel.Workbook()
# アクティブなワークシートを得る
sheet = book.active

# 連続でセルに値を設定する
for i in range(10):
    # セルに値を設定
    sheet.cell(row=(i+1), column=1, value=i)

# ファイルを保存
book.save("renzoku.xlsx")