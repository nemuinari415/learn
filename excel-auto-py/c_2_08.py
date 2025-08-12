import openpyxl as excel

# 売上データのブックを開いてシートを取り出す
book = excel.load_workbook("uriage.xlsx", data_only=True)
sheet = book.active

# A3からF9のセルを取り出す
rows = sheet["A3":"F9"]
for row in rows:
    # セルの値をリストとして得る
    values = [cell.value for cell in row]
    """
    values = []
    for cell in row:
        values.append(cell.value)
    """
    # リストを表示する
    print(values)