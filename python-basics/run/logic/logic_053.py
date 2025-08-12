# 人気の旅行先ランキングを集計
class TravelVoteAnalyzer:
    def __init__(self, votes):
        self.votes = votes
        self.result_data = {}

    def result_summary(self):
        for result in self.votes:
            user = result["user"]
            destination = result["destination"]

            if destination not in self.result_data:
                self.result_data[destination] = 0
            self.result_data[destination] += 1

    def print_result(self):
        rank = 1
        for destination, count in sorted(self.result_data.items(), key=lambda x: x[1], reverse=True):
            print(f"{rank}. {destination} - {count}票")
            rank += 1
