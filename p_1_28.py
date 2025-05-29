# p_1_27.py ファイルを読み込む
from p_1_27 import Circle

radius = int(input("半径を入力(cm) >>"))

c = Circle(radius)
c.area_calc()
c.circum_calc()
c.print_circle()