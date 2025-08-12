# 購入履歴のカテゴリ別件数を集計

purchases = [
    {"user": "田中", "item": "ノートパソコン", "category": "家電"},
    {"user": "佐藤", "item": "冷蔵庫", "category": "家電"},
    {"user": "鈴木", "item": "Tシャツ", "category": "衣類"},
    {"user": "田中", "item": "ズボン", "category": "衣類"},
    {"user": "佐藤", "item": "洗濯機", "category": "家電"},
    {"user": "中村", "item": "ジャケット", "category": "衣類"},
    {"user": "山田", "item": "炊飯器", "category": "家電"},
    {"user": "田中", "item": "帽子", "category": "衣類"},
]

p_data = {}


def count_by_category(purchases):

    for row in purchases:
        user = row["user"]
        item = row["item"]
        category = row["category"]

        if category not in p_data:
            p_data[category] = 0
        p_data[category] += 1
    return p_data


def print_summary(p_data):
    print("[ カテゴリ別購入数 ]")
    for category, count in p_data.items():
        print(f"{category} : {count}件")


p_data = count_by_category(purchases)
print_summary(p_data)
