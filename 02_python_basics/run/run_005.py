# logic_005.py ファイルを読み込む
from logic.logic_005 import JankenGame

game = JankenGame()
game.input_player()

while True:
    game.start_game()
    game.judge()
    
    if game.p1_c == game.p2_c:
        pass
    elif (game.p1_c == 1 and game.p2_c == 2) or \
        (game.p1_c == 2 and game.p2_c == 3) or \
        (game.p1_c == 3 and game.p2_c == 1):
        break
    else:
        break    

# bash
# PYTHONPATH=. python3 run/run_005.py