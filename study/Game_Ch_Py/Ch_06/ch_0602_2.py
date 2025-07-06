import tkinter

root = tkinter.Tk()
root.title("The First Label")
root.geometry("800x600")

# ラベルの作成と配置
label = tkinter.Label(root, text="ラベルの文字列",
                      font=("System", 24))
label.place(x=200, y=100)

root.mainloop()