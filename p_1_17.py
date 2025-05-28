# リスト内の各要素を2倍にする
class Data_list:
    def __init__(self, data):
        self.data = data
        self.map_data = []
    
    def map_lambda(self):
        result = list(map(lambda x: x * 2, self.data))
        self.map_data = result

    def print_data(self):
        print(f"入力 : {self.data}")
        print(f"出力 : {self.map_data}")