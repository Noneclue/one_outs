import tkinter as tk
import tkinter.ttk as ttk
import sys


def appexit():
    sys.exit()


def update_money():
    getset = tk.StringVar()
    getset = innings.get()
    money["text"] = getset


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
    bg="#00FF00",
    )
display.pack(fill=tk.X)

mid = tk.Frame(root)
update = tk.Button(mid, text="更新", command=update_money)
innings = tk.Spinbox(mid, from_=0, to=15, increment=1, width=4)
ary = ["0/3", "1/3", "2/3"]
one_third = tk.Spinbox(mid, value=ary, width=4, wrap=True)
er = tk.Spinbox(mid, from_=0, to=99, width=4)
# earned run = 自責点（英語）
money = tk.Label(mid, text="1試合の収支", relief="groove", width=16)
fix = tk.Button(mid, text="<<確定>>")

update.pack(padx=5, side="left")
innings.pack(side="left")
one_third.pack(side="left")
er.pack(padx=10, side="left")
money.pack(side="left")
fix.pack(padx=5, side="right")

mid.pack(pady=5, fill=tk.X,)

bot = tk.Canvas(root)
bar = tk.Scrollbar(root, orient=tk.VERTICAL)
bar.pack(side=tk.RIGHT, fill=tk.Y)
bar.config(command=bot.yview)

bot.config(yscrollcommand=bar.set)
bot.config(scrollregion=bot.bbox("all"))

calc = ttk.Treeview(bot)
bot.create_window((0, 0), window=calc, anchor=tk.NW, width=bot.cget("width"))

calc["columns"] = (1, 2, 3, 4)
calc["show"] = "headings"

calc.heading(1, text="登板機会")
calc.heading(2, text="投球回数")
calc.heading(3, text="自責点")
calc.heading(4, text="金銭収支")

calc.column(1, minwidth=60, width=80)
calc.column(2, minwidth=80, width=120)
calc.column(3, minwidth=60, width=120)
calc.column(4, minwidth=120, width=240)

calc.insert("", "end", values=("5/1", "9", "0"))
calc.insert("", "end", values=("5/6", "7 1/3", "3"))
calc.insert("", "end", values=("5/12", "6 2/3", "5"))

bot.pack(fill=tk.BOTH)
calc.pack()

root.mainloop()
