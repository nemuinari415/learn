import tkinter

root = tkinter.Tk()
root.title("The First Button")
root.geometry("800x600")

# ボタンの配置
button = tkinter.Button(root, text="ボタンの文字列",
                        font=("Time New Romen", 24))
button.place(x=200, y=100)

root.mainloop()