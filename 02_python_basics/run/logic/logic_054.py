# 映画レビュー集計クラス
class ReviewsAnalyzer:
    def __init__(self, reviews):
        self.reviews = reviews
        self.score_data = {}

    def reviews_summary(self):
        for rev in self.reviews:
            user = rev["user"]
            title = rev["title"]
            score = rev["score"]

            if title not in self.score_data:
                self.score_data[title] = [0, 0]  # score, count
            self.score_data[title][0] += score
            self.score_data[title][1] += 1

    def print_reviews(self):
        rank = 1
        print("映画レビュー平均評価（高評価順）")
        sorted_data = sorted(
            self.score_data.items(), key=lambda x: (-x[1][0] / x[1][1], x[0])  # 平均スコア降順、タイトル昇順
        )

        for title, (total, count) in sorted_data:
            avg = total / count
            print(f"{rank}. {title} - 平均 {avg:.1f}点")
            rank += 1
