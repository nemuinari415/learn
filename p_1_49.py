# アンケート集計アプリ（選択肢カウント）
import csv

class SurveyCounter:
    def __init__(self, votes):
        self.votes = votes

    def add_vote(self, language): # 投票を追加
        if language == 1:
            self.votes["Python"] += 1
        if language == 2:
            self.votes["Java"] += 1
        if language == 3:
            self.votes["C++"] += 1
        if language == 4:
            self.votes["JavaScript"] += 1
    
    def print_result(self):
        for lang, p in self.votes.items():
            print(f"{lang}, {p}")

    def write_results(self, filename):
        with open(filename, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["言語", "票数"]) # ヘッダー
            for lang, count in self.votes.items():
                writer.writerow([lang, count]) # 1行ずつ書き出し
        print("ファイルが出力されました。")