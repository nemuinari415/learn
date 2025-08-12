# logic_014.py ファイルを読み込む
from logic.logic_014 import Circle

radius = int(input("半径を入力(cm) >>"))

c = Circle(radius)
c.area_calc()
c.circum_calc()
c.print_circle()

# bash
# PYTHONPATH=. python3 run/run_014.py