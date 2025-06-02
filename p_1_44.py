# p_1_43.py ファイルを読み込む

from p_1_43 import SalesAggregator

filenames = "p_1_43_sales_log.csv"

sales_aggregator = SalesAggregator(filenames)
sales_aggregator.read_data()
sales_aggregator.print_summary()