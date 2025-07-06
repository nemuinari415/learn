import openpyxl as excel
import datetime

in_file = 'date-sample.xlsx'
out_file = 'date-wareki.xlsx'
cell_format = '[$-ja-JP]ggge"年"m"月"d"日"'

# メイン処理
def date_wareki(in_file, out_file):
    book = excel.load_workbook(in_file)
    for sheet in book.worksheets:
        for row in sheet.iter_rows():
            for cell in row:
                check_cell(cell)
    book.save(out_file)

def check_cell(cell):
    if type(cell.value) is datetime.datetime:
        cell.number_format = cell_format

if __name__ == '__main__':
    date_wareki(in_file, out_file)
