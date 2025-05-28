# #p_1_09.py ファイルを読み込む
from p_1_09 import JankenGame

# 実行
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