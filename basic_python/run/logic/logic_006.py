# 偶数だけをリストから抽出して表示する
class Even_Number:
    def __init__(self, numbers):
        self.numbers = numbers
        self.even_list = []
    
    def calc_num(self):
        for n in self.numbers:
            if n % 2 == 0:
                self.even_list.append(n)
        return self.even_list
    
    def print_even(self):
        print(f"偶数 : {self.even_list}")