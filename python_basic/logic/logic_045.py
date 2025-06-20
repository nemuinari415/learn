# ユーザーのログイン記録を集計する
class LoginTracker:
    def __init__(self, logs):
        self.logs = logs
        self.log_data = {}
        
    def group_by_time(self):
        for users in self.logs:
            user = users["user"]
            time = users["time"]

            if time not in self.log_data:
                self.log_data[time] = 0
            self.log_data[time] += 1
            
    def print_summary(self):
        print("時間帯別ログイン人数")
        for time in ["morning", "afternoon", "night"]:
            count = self.log_data.get(time, 0)
            print(f"{time}: {count}人")