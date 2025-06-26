# 以下のリストの内容を、1行ずつ
# words.txt というテキストファイルに書き込む。
class Words_list:
    def __init__(self, words):
        self.words = words
    
    def print_words(self):
        with open("folder_output/logic_002.txt", "w", encoding="utf-8", newline="") as f:
            for i, w in enumerate(self.words):
            # enumerate()
            # i : リストのインデックス（0から始まる番号）
            # w : リストの中の要素
                if i < len(self.words) - 1:
                    f.write(w + "\n") # 最後以外は改行つける
                else:
                    f.write(w) # 最後だけ改行なし