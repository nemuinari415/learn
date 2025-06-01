# テストの点数を分析するプログラム
import csv

class ScoreAnalyzer:
    def __init__(self, scores, filenames):
        self.filenames = filenames
        self.scores = scores
        self.total = 0

    def calc_scores(self):
        self.total = sum(self.scores)
        self.max_score = max(self.scores)
        self.min_score = min(self.scores)
        self.avg = self.total / len(self.scores)

    def print_scores(self):
        print("[テスト結果]")
        print(f"平均点 : {self.avg:.1f}点")
        print(f"最高点 : {self.max_score}点")
        print(f"最低点 : {self.min_score}点")
    
    def write_scores(self):
        try:
            with open(self.filenames, "w", encoding="utf-8", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["平均点", f"{self.avg:.1f}点"])
                writer.writerow(["最高点", f"{self.max_score}点"])
                writer.writerow(["最低点", f"{self.min_score}点"])
        except IOError as e:
            print("ファイル書き込みエラー:", e)
    
    def read_scores(self):
        print("CSVファイルを読み取る")
        with open(self.filenames, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                print(" : ".join(row))