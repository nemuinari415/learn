# リストの中から最大値と最小値を表示する関数
# min_max() を書いてください。
class Min_Max:
    def __init__(self, numbers):
        self.min_n = None
        self.max_n = None
        self.numbers = numbers

    def min_max_calc(self):
        self.min_n = min(self.numbers)
        self.max_n = max(self.numbers)
        return self.min_n, self.max_n
    
    def print_num(self):
        print(f"最小値 : {self.min_n}")
        print(f"最大値 : {self.max_n}")