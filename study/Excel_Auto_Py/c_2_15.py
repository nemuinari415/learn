import openpyxl as x1
# ブックを作りシートを得る
book = x1.Workbook()
sheet = book.active

# A1、B1、C1にすべて同じ値を設定
val = 3.14159
sheet.append([val, val, val])

# 小数点以下を省略して表示
sheet["A1"].number_format = "0"
sheet["B1"].number_format = "0.00"
sheet["C1"].number_format = "0.0000"

# 保存
book.save("number_format.xlsx")