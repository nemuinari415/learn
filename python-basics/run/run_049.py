# logic_049.py ファイルを読み込む
from logic.logic_049 import Questionnaire

answers = [
    {"user": "田中", "fruit": "りんご"},
    {"user": "佐藤", "fruit": "バナナ"},
    {"user": "鈴木", "fruit": "りんご"},
    {"user": "山田", "fruit": "みかん"},
    {"user": "高橋", "fruit": "バナナ"},
    {"user": "中村", "fruit": "りんご"}
]

q = Questionnaire(answers)
q.survey_result()
q.print_result()

# bash
# PYTHONPATH=. python3 run/run_049.py