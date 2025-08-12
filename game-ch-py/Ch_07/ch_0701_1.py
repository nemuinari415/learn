import tkinter

root = tkinter.Tk()
root.title("初めてのテキスト入力欄")
root.geometry("400x200")

# 入力欄の部品を作る
entry = tkinter.Entry(width=20)
entry.place(x=10, y=10)

root.mainloop()