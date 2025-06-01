# ToDoリスト管理アプリ（簡易版）
class ToDoManager:
    def __init__(self):
        self.todo_list = []
    
    def add_task(self):
        while True:
            task = input("新しいタスクを入力 >>")
            due = input("期限を入力(例:2025-05-23) >> ")
            self.todo_list.append({"task": task, "due": due})

            i = input("追加しますか？(y | n) >>")
            if i.lower() != "y": # i を小文字にする
                break

    def show_tasks(self):
        print("[ 現在のTodoリスト ]" + "\n")
        for item in self.todo_list:
            print(f"{item["task"]} (期限:{item["due"]})")