# p_1_39.py ファイルを読み込む
from p_1_39 import SalesCalculator

file_name = "p_1_39_sales.csv"

sales_calculator = SalesCalculator(file_name)
sales_calculator.read_csv()
sales_calculator.calc_total()
sales_calculator.print_result()