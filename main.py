import tkinter as tk
import tkinter.ttk as ttk
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

mid = tk.Canvas(root)
bar = tk.Scrollbar(root, orient=tk.VERTICAL)
bar.pack(side=tk.RIGHT, fill=tk.Y)
bar.config(command=mid.yview)

mid.config(yscrollcommand=bar.set)
mid.config(scrollregion=(0, 0, 400, 500))
mid.pack(side=tk.LEFT, fill=tk.BOTH)

calc = ttk.Treeview(mid)
mid.create_window((0, 0), window=calc, anchor=tk.NW, width=mid.cget("width"))

calc["columns"] = (1, 2, 3)
calc["show"] = "headings"

calc.heading(1, text="登板日")
calc.heading(2, text="投球回数")
calc.heading(3, text="自責点")

calc.insert("", "end", values=("5/1", "9", "0"))
calc.insert("", "end", values=("5/6", "7 1/3", "3"))
calc.insert("", "end", values=("5/12", "6 2/3", "5"))

calc.pack()

root.mainloop()
