import openpyxl as excel

# 新規ワークブックを作りワークシートを得る
book = excel.Workbook()
sheet = book.active

# 連続でセルに値を設定する
for y in range(1, 21):
    for x in range(1, 21):
        # セルを取得して値を設定
        cell = sheet.cell(y, x)
        cell.value = x * y

#ファイルを保存
book.save("20x20.xlsx")