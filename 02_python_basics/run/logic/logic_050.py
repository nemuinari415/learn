# ユーザー別の購入履歴を集計するクラス
class PurchaseHistory:
    def __init__(self, logs):
        self.logs = logs
        self.users_data = {}
        
    def add_logs(self):
        for log in self.logs:
            user = log['user']
            item = log['item']
            price = log['price']

            if user not in self.users_data:
                self.users_data[user] = [[], 0] # item = strなのでappendできない為
                
            self.users_data[user][0].append(item)
            self.users_data[user][1] += price

    def print_summary(self):
        for users, (item, total) in self.users_data.items():
            print(f'{users}:')
            print(f'  購入アイテム: {",".join(item)}')
            print(f'  合計金額: {total}円')