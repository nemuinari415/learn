# 2つの辞書をマージし、すべてのキーと値を出力
class Dict_Marge:
    def __init__(self, dict_a, dict_b):
        self.dict_a = dict_a
        self.dict_b = dict_b
        self.mar = {}

    def marges(self):
        self.mar = {**self.dict_a, **self.dict_b}
        return self.mar
    
    def print_marges(self):
        for key, value in self.mar.items():
            print(f"{key} : {value}")