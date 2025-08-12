import tkinter

root = tkinter.Tk()
root.title("The First Canvas")

# キャンバスの作成
canvas = tkinter.Canvas(root, width=400, height=600,
                        bg="skyblue")
canvas.pack()
root.mainloop()