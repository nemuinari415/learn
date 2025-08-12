# logic_026.py ファイルを読み込む
from logic.logic_026 import FolderScanner

folder_path = input("フォルダのパスを入力 >>")
# ./sample_folder など

filename = "folder_output/" + "logic_026" + ".csv"

folder_scanner = FolderScanner(folder_path)
folder_scanner.scan_files()
folder_scanner.save_to_csv(filename)
folder_scanner.print_summary(filename)

# bash
# PYTHONPATH=. python3 run/run_026.py