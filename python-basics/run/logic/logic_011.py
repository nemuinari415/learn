# 辞書で名簿検索
class Phone_Books:
    def __init__(self, phone_book, name):
        self.phone_book = phone_book
        self.name = name

    def print_book(self):
        print(f"{self.name}さん： {self.phone_book[self.name]}")