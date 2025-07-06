import openpyxl as excel

book = excel.Workbook()
sheet = book.active

# セル名から行番号 / 列番号を得る
cell = sheet["C2"]
(row, col) = (cell.row, cell.column)
print("C2 = ({},{})".format(row, col))

# 行番号/列番号からセル名を得る
cell = sheet.cell(row = 2, column = 3)
cdt = cell.coordinate
print("(2,3) = {}".format(cdt))