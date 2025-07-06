#データ構造 スタックについて
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        last = len(self.items)-1
        return self.items[last]

    def size(self):
        return len(self.items)

number_list = [1, 2, 3, 4, 5]
stack = Stack()

for c in number_list:
    stack.push(c)

reverse = []

while stack.size():
    reverse.append(stack.pop())

print(reverse)