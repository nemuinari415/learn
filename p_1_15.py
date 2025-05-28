# 与えられた文字列が回文か判定する
class Palindrome:
    def __init__(self):
        self.word = ""
        self.word_copy = ""
        self.p = None

    def input_word(self):
        self.word = input("文字を入力 >>")
        self.word_copy = self.word
        self.word = self.word[::-1]
        return self.word, self.word_copy

    def is_palindrome(self):
        if self.word == self.word_copy:
            self.p = True
        else:
            self.p = False
        return self.p
    
    def print_p(self):
        if self.p == True:
            print(f"入力 : {self.word_copy} / 出力 : {self.word} = {self.p}")
        else:
            print(f"入力 : {self.word_copy} / 出力 : {self.word} = {self.p}")