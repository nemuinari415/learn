# run_054.py ファイルを読み込み
from logic.logic_054 import ReviewsAnalyzer

reviews = [
    {"user": "田中", "title": "インセプション", "score": 5},
    {"user": "佐藤", "title": "インセプション", "score": 4},
    {"user": "鈴木", "title": "アバター", "score": 3},
    {"user": "山田", "title": "アバター", "score": 5},
    {"user": "中村", "title": "ダークナイト", "score": 4},
]

ra = ReviewsAnalyzer(reviews)
ra.reviews_summary()
ra.print_reviews()
