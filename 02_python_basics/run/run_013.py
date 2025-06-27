# logic_013.py ファイルを読み込む
from logic.logic_013 import Write_Files

lines = ["こんにちは", "Pythonを学習中です", "ファイルに書き込みます"]

write_files = Write_Files(lines)
write_files.write_file()

# bash
# PYTHONPATH=. python3 run/run_013.py