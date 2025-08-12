class InputNumbers:
    def __init__(self):
        self.num_a = None
        self.num_b = None

    def input_numbers(self):
        try:
            self.num_a = int(input("1つ目の数値を入力 >>"))
            self.num_b = int(input("2つ目の数値を入力 >>"))
        except ValueError:
            print("整数を入力してください")
            return None, None
        return self.num_a, self.num_b
