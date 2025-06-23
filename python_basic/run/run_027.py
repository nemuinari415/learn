# logic_027.py ファイルを読み込む
from logic.logic_027 import ExtensionCounter

folder_path = "./folder_output"
filename = "folder_output/" + "logic_027" + ".csv"

extension_counter = ExtensionCounter(folder_path)
extension_counter.scan_folder()
extension_counter.print_summary()
extension_counter.write_summary(filename)

# bash
# PYTHONPATH=. python3 run/run_027.py