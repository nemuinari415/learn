# logic_053.py ファイルを読み込む
from logic.logic_053 import TravelVoteAnalyzer

votes = [
    {"user": "田中", "destination": "沖縄"},
    {"user": "山田", "destination": "北海道"},
    {"user": "佐藤", "destination": "沖縄"},
    {"user": "鈴木", "destination": "京都"},
    {"user": "高橋", "destination": "北海道"},
    {"user": "伊藤", "destination": "沖縄"},
    {"user": "渡辺", "destination": "京都"},
    {"user": "中村", "destination": "北海道"},
]

tva = TravelVoteAnalyzer(votes)
tva.result_summary()
tva.print_result()
