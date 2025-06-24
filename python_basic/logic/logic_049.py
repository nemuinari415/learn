# アンケート集計
class Questionnaire:
    def __init__(self, answers):
        self.answers = answers
        self.result_data = {}
    
    def survey_result(self):
        for item in self.answers:
            user = item['user']
            fruit = item['fruit']

            if fruit not in self.result_data:
                self.result_data[fruit] = {}
            if user not in self.result_data[fruit]:
                self.result_data[fruit][user] = 1
            else:
                self.result_data[fruit][user] += 1
    
    def print_result(self):
        print("アンケート結果")
        for fruit, user in self.result_data.items():
            print(f"{fruit} : {len(user.values())}人")