import tkinter

def click_btn():
    button["text"] = "クリックしました"

root = tkinter.Tk()
root.title("The First Button")
root.geometry("800x600")

# command = クリック時に働く関数
button = tkinter.Button(root, text="クリックしてください",
                        font=("Times New Romen", 24),
                        command=click_btn)
button.place(x=200, y=100)

root.mainloop()