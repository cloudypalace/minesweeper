from cell import Cell
from board import Board
import os
import tkinter as tk
from tkinter import messagebox


rows =9
cols = 9
mines =10

board = Board(rows=rows,cols=cols,mines=mines)


def reveal(i, j):
    result = board.reveal(i, j)
    refresh_ui()
    if not result:
        tk.messagebox.showinfo("游戏结束", "你输了！")
        
    win = board.check_win()
    if win:
        tk.messagebox.showinfo("游戏结束", "你赢了！")



def flag(i, j, event):    # event 是 bind 传进来的
    board.toggle_flag(i, j)
    refresh_ui()

def refresh_ui():
    for i in range(rows):
        for j in range(cols):
            cell = board.My_Borad[i][j]
            btn = buttons[i][j]
            if cell.is_revealed:
                if cell.is_mine:
                    btn.config(text="💣", relief="sunken",bg="#BC1313")
                elif cell.adjacent_mines > 0:
                    btn.config(text=str(cell.adjacent_mines), relief="sunken",bg="#D7DFE7")
                else:
                    btn.config(text="", relief="sunken",bg="#D7DFE7")
            elif cell.is_flagged:
                btn.config(text="🚩", relief="raised",bg="#767C83")
            else:
                btn.config(text="",relief="raised",bg="#767C83")
            

root = tk.Tk()
root.title("扫雷")

# menubar = tk.Menu(root)

# settings_menu = tk.Menu(menubar, tearoff=0)
# settings_menu.add_command(label="偏好设置…", command=lambda: print("打开设置"))
# settings_menu.add_separator()
# settings_menu.add_command(label="退出", command=root.quit)
# menubar.add_cascade(label="设置", menu=settings_menu)

buttons = [[None]*cols for _ in range(rows)]
for i in range(rows):
    for j in range(cols):
        btn = tk.Button(root, text="", width=2, height=1, command=lambda i=i, j=j: reveal(i, j),bg="#767C83")
        btn.grid(row=i, column=j)
        btn.bind("<Button-3>", lambda event, i=i, j=j: flag(i, j, event))
        buttons[i][j] = btn

# root.config(menu=menubar)

root.mainloop()
