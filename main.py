import tkinter as tk
import sys


def appexit():
    sys.exit()


root = tk.Tk()
root.geometry("640x480")
root.title("ワンナウツ契約計算機")

menubar = tk.Menu(root)
menu1 = tk.Menu(menubar, tearoff=False)
menu1.add_command(label="新規")
menu1.add_separator()
menu1.add_command(label="終了", command=appexit)

menubar.add_cascade(label="ファイル", menu=menu1)
root["menu"] = menubar

display = tk.Label(
    root,
    text="ここに年俸が表示されます",
    font=("メイリオ", 32, "bold"),
    fg="#FF0000",
    bg="#00FF00"
    )

display.pack(fill="x")


root.mainloop()
