import tkinter as tk
import tkinter.ttk as ttk
import sys


def appexit():
    sys.exit()


def update_money():
    income = tk.StringVar()
    ini = int(innings.get())
    third = 0
    lost = int(er.get())
    get_one_third = one_third.get()

    if get_one_third == "1/3":
        third = 1
    elif get_one_third == "2/3":
        third = 2
    else:
        third = 0

    income = str(500 * ((ini * 3) + third) - 5000 * lost)
    money["text"] = income + "万円"


def update_money_after():
    income = tk.StringVar()
    ini = int(innings.get())
    third = 0
    lost = int(er.get())
    get_one_third = one_third.get()

    if get_one_third == "1/3":
        third = 1
    elif get_one_third == "2/3":
        third = 2
    else:
        third = 0

    income = str(500 * ((ini * 3) + third) - 5000 * lost)
    money["text"] = income + "万円"

    root.after(500, update_money_after)


def refresh():
    pass


def fix():
    add = 0
    innings_str = innings.get() + "回 " + one_third.get()
    er_str = str(er.get())
    money_str = money["text"]
    calc.insert("", "end", values=(add, innings_str, er_str, money_str))

    innings_var = tk.StringVar(value="0")
    one_third_var = tk.StringVar(value="0/3")
    er_var = tk.StringVar(value="0")

    innings["textvariable"] = innings_var
    one_third["textvariable"] = one_third_var
    er["textvariable"] = er_var

    refresh()


root = tk.Tk()
root.geometry("640x240")
root.title("ワンナウツ契約計算機")

root.minsize(480, 200)
root.maxsize(1280, 480)

menubar = tk.Menu(root)
menu1 = tk.Menu(menubar, tearoff=False)
menu1.add_command(label="新規")
menu1.add_separator()
menu1.add_command(label="終了", command=appexit)

menubar.add_cascade(label="ファイル", menu=menu1)
root["menu"] = menubar

# グリーンバック用ラベル
display = tk.Label(
    root,
    text="ここに年俸が表示されます",
    font=("メイリオ", 32, "bold"),
    fg="#FF0000",
    bg="#00FF00",
    )
display.pack(fill=tk.X)

# 成績登録用スピンボックスと登録ボタン
mid = tk.Frame(root)

update = tk.Button(mid, text="更新", command=refresh)
inning_label = tk.Label(mid, text="投球回:")
innings = tk.Spinbox(
    mid, from_=0, to=15, increment=1, width=4)
ary = ["0/3", "1/3", "2/3"]
one_third = tk.Spinbox(mid, value=ary, width=4, wrap=True)
er_label = tk.Label(mid, text="失点:")
er = tk.Spinbox(mid, from_=0, to=99, width=4)
# earned run = 自責点（英語）
money = tk.Label(mid, text="1試合の収支", relief="groove", width=16)
fix_button = tk.Button(mid, text="<<確定>>", command=fix)

update.pack(padx=5, side="left")
inning_label.pack(padx=5, side=tk.LEFT)
innings.pack(side="left")
one_third.pack(side="left")
er_label.pack(padx=5, side="left")
er.pack(side="left")
money.pack(side="left")
fix_button.pack(padx=5, side="right")

mid.pack(pady=5, fill=tk.X,)

# 成績一覧用ツリービューとスクロールバー
bot = tk.Frame(root, relief="sunken")
bot.pack(fill=tk.BOTH)

calc = ttk.Treeview(bot)
calc["columns"] = (1, 2, 3, 4)
calc["show"] = "headings"
calc["height"] = 18

calc.heading(1, text="登板機会")
calc.heading(2, text="投球回数")
calc.heading(3, text="自責点")
calc.heading(4, text="金銭収支")

calc.column(1, minwidth=60, width=60)
calc.column(2, minwidth=80, width=160)
calc.column(3, minwidth=80, width=160)
calc.column(4, minwidth=120, width=240)

y_bar = tk.Scrollbar(bot, orient=tk.VERTICAL, command=calc.yview)
y_bar.pack(side=tk.RIGHT, fill=tk.Y)

calc.pack(fill=tk.BOTH)
calc.config(yscrollcommand=y_bar.set)

# 成績更新用　スピンボックスのイベントに入れるべきか？
update_money_after()

root.mainloop()
