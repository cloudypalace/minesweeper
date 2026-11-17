class Cell:
    is_mine:bool
    is_revealed:bool
    is_flagged:bool
    adjacent_mines:int
    def __init__(self):
        self.is_mine = False
        self.is_revealed = False
        self.is_flagged = False
        self.adjacent_mines = 0
