import tkinter

root = tkinter.Tk()
root.title("チェックボタンを扱う")
root.geometry("400x200")

# チェックボタンの部品を作る
cbtn = tkinter.Checkbutton(text="チェックボタン")
cbtn.pack()

root.mainloop()