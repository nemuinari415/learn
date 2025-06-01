# p_1_41.py ファイルを読み込む
from p_1_41 import ScoreAnalyzer

scores = [70, 82, 65, 92, 83, 78]
filenames = "scores.csv"

score_analyzer = ScoreAnalyzer(scores, filenames)
score_analyzer.calc_scores()
score_analyzer.print_scores()
score_analyzer.write_scores()
score_analyzer.read_scores()