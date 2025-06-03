# ユーザーが入力した整数を逆順のリストにして表示
class Revers_Num_List:
    def __init__(self, num_list):
        self.num_list = num_list

    def revers_num(self):
        r = list(reversed(self.num_list))
        print(f"入力 : {self.num_list}")
        print(f"出力 : {r}")