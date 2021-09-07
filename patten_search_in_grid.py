class Grid():
    def __init__(self,grid,p):
        self.grid = grid
        self.x = 0
        self.y = 0
        self.current = hash(self.grid)
        self.p = p
        self.hp = hash(self.p)
    def hash(x):
        return sum(sum(x[i][j] for i in range(3)) for j in range(3))
    def match(self):
        if self.current == self.hp:
            #TODO : real check of equality
            if 1:
                return True
        else:
            return False
    def next(self):
        for i in range(3):
            self.current -= self.grid[self.x][self.y-i]
            self.current += self.grid[self.x+3][self.y-i]

x= Grid([[1,2,1],[1,2,1],[1,2,1],[1,2,1]])