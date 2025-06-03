# クラス Circle を作って半径を渡すと面積と円周を返す
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius # 半径
    
    def area_calc(self):
        self.area = math.pi * self.radius ** 2
    
    def circum_calc(self):
        self.circum = math.pi * 2 * self.radius

    def print_circle(self):
        print(f"半径 : {self.radius}㎝")
        print(f"面積 : {self.area:.1f}㎠")
        print(f"円周 : {self.circum:.1f}㎝")