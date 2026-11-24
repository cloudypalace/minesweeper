from cell import Cell
from board import Board
import os
import tkinter as tk
from tkinter import messagebox

flag_judgment = True


rows =10
cols = 10
mines =10

board = Board(rows=rows,cols=cols,mines=mines)


def reveal(i, j, root):
    result = board.reveal(i, j)
    refresh_ui()
    if flag_judgment and not result:
        str = "游戏结束,你输了！"
        open_modal_window(root,str)
        
    win = board.check_win()
    if win:
        if flag_judgment == True:
            str = "游戏结束,你赢了！"
        else:
            str = "游戏结束"
        open_modal_window(root,str)
        root.destroy()

def open_modal_window(root,str):

    def go_on():
        global flag_judgment
        flag_judgment = False
        modal.destroy()

    def go_end():
        modal.destroy()
        root.destroy()

    
    modal = tk.Toplevel(root)
    modal.grab_set()

    label = tk.Label(modal,text=str)
    label.pack(pady=(20,10))

    #btn1 = tk.Button(modal,text="再来一局")
    btn2 = tk.Button(modal,text="继续",command=go_on)
    btn3 = tk.Button(modal,text="结束",command=go_end)
    #btn1.pack()
    btn2.pack()
    btn3.pack()

    root.wait_window(modal)




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
        btn = tk.Button(root, text="", width=2, height=1, command=lambda i=i, j=j: reveal(i, j, root),bg="#767C83")
        btn.grid(row=i, column=j)
        btn.bind("<Button-3>", lambda event, i=i, j=j: flag(i, j, event))
        buttons[i][j] = btn

# root.config(menu=menubar)

root.mainloop()
