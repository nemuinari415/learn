# 名前と年齢を引数で受け取り、「〇〇さんは〇歳です」と出力する
class Info_Profile:
    def __init__(self):
        self.name = None
        self.age = None
    
    def input_profile(self):
        while True:
            try:
                self.name = str(input("名前を入力してください >>"))
                self.age = int(input("年齢を入力してください >>"))
                break
            except ValueError:
                print("入力ミスです")
    
    def print_profile(self):
        print(f"{self.name}さんは、{self.age}歳です")