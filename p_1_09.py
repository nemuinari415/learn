#じゃんけん
import random

class JankenGame:
    def __init__(self):
        self.p1 = ""
        self.p2 = ""
        self.p1_c = 0
        self.p2_c = 0
        self.hands = {1: "グー", 2: "チョキ", 3: "パー"}

    def input_player(self):
        self.p1 = input("あなたの名前 >> ")
        self.p2 = "コンピュータ"

    def start_game(self):
        print("最初はグー！じゃんけん...")
        while True:
            try:
                choice = int(input("あなたの手を選んでください [1:グー, 2:チョキ, 3:パー] >> "))
                if choice in [1, 2, 3]:
                    self.p1_c = choice
                    break
                else:
                    print("1〜3の数字で選んでください。")
            except ValueError:
                print("数値を入力してください。")

        self.p2_c = random.choice([1, 2, 3])
        print(f"{self.p1}：{self.hands[self.p1_c]} vs {self.p2}：{self.hands[self.p2_c]}")

    def judge(self):
        if self.p1_c == self.p2_c:
            print("あいこです。")
        elif (self.p1_c == 1 and self.p2_c == 2) or \
             (self.p1_c == 2 and self.p2_c == 3) or \
             (self.p1_c == 3 and self.p2_c == 1):
            print(f"{self.p1} の勝ちです！")
        else:
            print(f"{self.p2} の勝ちです！")