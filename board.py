from cell import Cell
import random
class Board:

    mines:int
    My_Borad:list
    rows:int
    cols:int

    #检查是否越界
    def is_valid(self,nx,ny):
        if 0<= nx < self.rows and 0<= ny< self.cols:
            return True
        else:
            return False
        
    #放雷
    def put_mine(self,mines):
        i=0
        while i < mines:
            x=random.randint(0,self.rows-1)
            y=random.randint(0,self.cols-1)
            if not self.My_Borad[x][y].is_mine:
                self.My_Borad[x][y].is_mine = True
                i+=1


    #检测周围雷
    def find_round_mines(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:  # 跳过自己
                    continue
                nx, ny = x + dx, y + dy
                if self.is_valid(nx, ny) and self.My_Borad[nx][ny].is_mine:
                    count += 1
        return count


    #类初始化
    def __init__(self,rows:int,cols:int,mines:int):
        #数据初始化
        self.rows=rows
        self.cols=cols
        self.My_Borad = [[Cell() for _ in range(cols)] for _ in range(rows)]
        self.mines = mines


        #放雷
        self.put_mine(mines)


        #更新周围雷的数量
        for i in range(0,rows):
            for j in range(0,cols):
                self.My_Borad[i][j].adjacent_mines = self.find_round_mines(i,j)

    #翻格子
    def reveal(self,row,col):
        if self.My_Borad[row][col].is_revealed or self.My_Borad[row][col].is_flagged:
            return True
        elif self.My_Borad[row][col].is_mine:
            self.My_Borad[row][col].is_revealed = True
            return False
        else:
            self.My_Borad[row][col].is_revealed = True
            if self.My_Borad[row][col].adjacent_mines ==0:
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if dx == 0 and dy == 0:  # 跳过自己
                            continue 
                        row1 = row+dx
                        col1 = col+dy
                        if self.is_valid(row1,col1) and (not self.My_Borad[row1][col1].is_revealed) :
                            self.reveal(row1,col1)
            return True

    #标记/取消标记
    def toggle_flag(self,row,col):
        if self.My_Borad[row][col].is_revealed:
            return 
        if not self.My_Borad[row][col].is_flagged:
            self.My_Borad[row][col].is_flagged = True
        else:
            self.My_Borad[row][col].is_flagged = False

    #胜利
    def check_win(self):
        for x in range(self.rows):
            for y in range(self.cols):
                if not self.My_Borad[x][y].is_mine and not self.My_Borad[x][y].is_revealed:
                    return False
        return True