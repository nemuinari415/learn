import openpyxl as excel

book = excel.Workbook()
sheet = book.active

# A1のセルに日付を設定
sheet["A1"] = "2023/01/01"
# B2のセルに計算式を設定
sheet["B1"] = '=TEXT(A1, "ggge年m月d日")'

# ワークブックを保存
book.save("susiki.xlsx")