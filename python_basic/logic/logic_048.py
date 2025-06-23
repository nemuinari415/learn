# ログデータからアクティビティを集計
class LogAnalyzer:
    def __init__(self, logs):
        self.logs = logs
        self.user_actions = {}
        
    def logs_totalling(self):
        for log in self.logs:
            user = log["user"]
            action = log["action"]

            if user not in self.user_actions:
                self.user_actions[user] = {}
            if action not in self.user_actions[user]:
                self.user_actions[user][action] = 1
            else:
                self.user_actions[user][action] += 1
            
    def print_totalling(self):
        print('ユーザー別アクション集計:')
        for users, actions in self.user_actions.items():
            actions_str = ','.join([f"{act}({cnt}回)" for act, cnt in actions.items()])
            print(f'{users} : {actions_str}') 
            