import tkinter

# コメントを出力する
KEKKA = [
    "前世がネコだった可能性は極めて薄いです。",
    "いたって普通の人間です。",
    "特別、おかしなところはありません。",
    "やや、ネコっぽいところがあります。",
    "ネコにかなり近い性格です。",
    "前世はネコだったかもしれません。",
    "見た目は人間、中身はネコの可能性があります。"
]

# チェックされたボタンを数える
def click_btn():
    pts = 0
    for i in range(7):
        if bvar[i].get() == True:
            pts = pts + 1
        nekodo = int(100 * pts/7)
        text.delete("1.0", tkinter.END)
        text.insert("1.0", "< 診断結果 >\n" \
        "貴方のネコ度は" + str(nekodo) + "%です。\n" + KEKKA[pts])
        text.insert("1.0", "チェックの数は" + str(pts))

# GUI の配置
root = tkinter.Tk()
root.title("ネコ度診断アプリ")
root.resizable(False, False)

canvas = tkinter.Canvas(root, width=800, height=600)
canvas.pack()

gazou = tkinter.PhotoImage(file="sumire.png")
canvas.create_image(400, 300, image=gazou)

button = tkinter.Button(text="診断する",
font=("Times New Roman", 32), bg="lightgreen", command=click_btn)
button.place(x=400, y=480)

text = tkinter.Text(width=30, height=5,
font=("Times New Roman", 16))

text.place(x=320, y=30)

# 複数のチェックボタンの配置
bvar = [None]*7
cbtn = [None]*7

ITEM = [
"高いところが好き",
"ボールを観ると転がしたくなる",
"びっくりすると髪の毛が逆立つ",
"ネズミの玩具が気になる",
"匂いに敏感",
"魚の骨をしゃぶりたくなる",
"夜、元気になる"
]

for i in range(7):
    bvar[i] = tkinter.BooleanVar()
    bvar[i].set(False)
    cbtn[i] = tkinter.Checkbutton(text=ITEM[i],font=("Times New Roman", 12),variable=bvar[i],bg="#dfe")
    cbtn[i].place(x=400, y=160 + 40 * i)

root.mainloop()