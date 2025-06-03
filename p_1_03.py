# Rectangle クラスを作成し、width と height を受け取り、
# area() メソッドで面積を返す。
class Rectangle:
    def __init__(self):
        self.width = None
        self.height = None

    def input_v(self):
        self.width = int(input("横の長さ(cm) >>"))
        self.height = int(input("縦の長さ(cm) >>"))
    
    def area(self):
        self.a = self.height * self.width
        return self.a
    
    def print_v(self):
        print(f"面積 : {self.area()}㎠") 