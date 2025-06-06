#ユーザーから数値を入力し、偶数なら "偶数です"
# 奇数なら "奇数です" と表示する関数 
class Even_odd_num:
    def __init__(self):
        self.number = None

    def input_number(self):
        while True:
            try:
                self.number = int(input("数値を入力 >>"))
                break
            except ValueError:
                print("入力ミスです。")

    def check_even_odd(self):
        if self.number % 2 == 0:
            print(f"{self.number}は、偶数です。")
        else:
            print(f"{self.number}は、奇数です。")