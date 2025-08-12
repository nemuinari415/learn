import tkinter
import random

# ボタンをクリックした時に呼び出す関数
def click_btn():
    label["text"]=random.choice(["大吉", "中吉", "小吉", "凶"])
    label.update()

# ウィンドウを作成
root = tkinter.Tk()
root.title("Omikuji_Soft")

# ウィンドウサイズを固定
root.resizable(False, False)

# キャンバスを作成
canvas = tkinter.Canvas(root, width=800, height=600)
canvas.pack()

# 画像を表示
gazou = tkinter.PhotoImage(file="miko.png")
canvas.create_image(400, 300, image=gazou)

# ラベルを作成
label = tkinter.Label(root, text="？？",
                      font=("Times New Roman", 120), bg="white")
label.place(x=380, y=60)

# ボタンを作成
button = tkinter.Button(root, text="おみくじを引く",
                        font=("Times New Roman", 36),
                        command=click_btn, fg="skyblue")
button.place(x=360, y=400)

root.mainloop()