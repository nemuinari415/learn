# 担当者別・売上合計の集計
import csv

class StaffSalesSummary:
    def __init__(self, read_filename, write_filename):
        self.r_fn = read_filename
        self.w_fn = write_filename
        self.staff_data = {}

    def read_csv(self):
        try:
            with open(self.r_fn, "r", encoding="utf-8", newline="") as f:
                reader = csv.reader(f)
                next(reader)  # ヘッダーをスキップ

                for row in reader:
                    try:
                        name = row[3]
                        value = int(row[1])
                        amount = int(row[6])
                        total = value * amount
                        self.staff_data[name] = self.staff_data.get(name, 0) + total
                    except (ValueError, IndexError):
                        continue  # 不正なデータをスキップ

            print("ファイルを読み込みました。")
        except FileNotFoundError:
            print(f"ファイルが見つかりません: {self.r_fn}")

    def write_csv(self):
        try:
            with open(self.w_fn, "w", encoding="utf-8", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["担当者", "売上"])

                # 売上順にソート
                for name, price in sorted(self.staff_data.items(), key=lambda x: x[1], reverse=True):
                    writer.writerow([name, price])

            print("ファイルを書き出しました。")
        except Exception as e:
            print("書き込み中にエラー:", e)