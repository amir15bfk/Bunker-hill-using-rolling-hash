class Grid():
    def __init__(self,grid,p):
        self.grid = grid
        self.x = 0
        self.y = 0
        self.mw = 1
        self.p = p
        self.current = self.hash(self.grid)
        self.hp = self.hash(self.p)
        self.done = False
    def hash(self,x):
        return sum(sum(x[i][j] for i in range(len(self.p))) for j in range(len(self.p[0])))
    def match(self):
        if self.current == self.hp:
            #TODO : real check of equality
            if 1:
                return True
        else:
            return False
    def next(self):
        if not self.done:
            if self.x+len(self.p)<len(self.grid) and 0<=self.x:
                for i in range(len(self.p[0])):
                    self.current -= self.mw*self.grid[self.x][self.y+i]
                    self.current += self.mw*self.grid[self.x+len(self.p)][self.y+i]
                self.x+=self.mw
            else:
                self.next_y()
                self.x -= self.mw
                self.mw*=-1
            
    def next_y(self):
        if self.y+len(self.p[0])<len(self.grid):
            for i in range(len(self.p)):
                self.current -= self.grid[self.x+i][self.y]
                self.current += self.grid[self.x+i][self.y+len(self.p[1])]
            self.y+=1
        else:
            self.done = True



x= Grid([[1,2,1,1],[1,2,1,1],[1,2,1,1],[1,3,1,1]],[[1,2,1],[1,2,1],[1,2,1]])
print(x.match())
x.next()
print(x.match())
x.next()
print(x.match())
x.next()
print(x.match())
x.next()
print(x.match())
x.next()
print(x.match())
x.next()
print(x.match())
x.next()
print(x.match())
