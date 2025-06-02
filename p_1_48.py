# p_1_47.py ファイルを読み込む
from p_1_47 import SalesAnalyzer

filenames = "p_1_47_sales.csv"

sales_analyzer = SalesAnalyzer(filenames)
sales_analyzer.read_csv_data()
sales_analyzer.calculate_total_sales()
sales_analyzer.print_csv_data()