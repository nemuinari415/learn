# ファイルに複数行を書き込む関数
class Write_Files:
    def __init__(self, lines):
        self.lines = lines

    def write_file(self):
        with open("folder_output/logic_013.txt", "w", encoding="utf-8", newline="") as f:
            for i, li in enumerate(self.lines):
                if i < len(self.lines) - 1:
                    f.write(f"{li} \n") # 改行あり
                else:
                    f.write(f"{li}") # 最後の行は改行なし