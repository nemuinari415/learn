# logic_021.py ファイルを読み込む
from logic.logic_021 import ScoreAnalyzer

scores = [70, 82, 65, 92, 83, 78]
filenames = "folder_output/" + "logic_021" + ".csv"

score_analyzer = ScoreAnalyzer(scores, filenames)
score_analyzer.calc_scores()
score_analyzer.print_scores()
score_analyzer.write_scores()
score_analyzer.read_scores()

# bash
# PYTHONPATH=. python3 run/run_021.py