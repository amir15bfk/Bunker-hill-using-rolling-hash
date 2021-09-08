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
        self.count = 0 
        self.where = []
        self.not_col_done = True
    def hash(self,x):
        return sum(sum(x[i][j] for i in range(len(self.p))) for j in range(len(self.p[0])))
    def match(self):
        if self.current == self.hp:
            #TODO : real check of equality
            for i in range(len(self.p)):
                for j in range(len(self.p[0])):
                    if self.grid[self.x+i][self.y+j]!=self.p[i][j]:
                        return False

            if 1:
                self.count += 0 
                self.where.append((self.x,self.y))
                return True
        else:
            return False
    def next(self):
        if not self.done:
            if self.x+len(self.p)<len(self.grid) and 0<=self.x and self.not_col_done:
                for i in range(len(self.p[0])):
                    self.current -= self.mw*self.grid[self.x][self.y+i]
                    self.current += self.mw*self.grid[self.x+len(self.p)][self.y+i]
                if self.x+len(self.p)<len(self.grid) and self.mw ==1:
                    self.x+=self.mw
                else:
                    self.not_col_done = False
                    self.mw*=-1 
            else:
                self.next_y()
                self.not_col_done = True
                
    def draw(self):
        for i in range(len(self.p)):
                for j in range(len(self.p[0])):
                    print(self.grid[self.x+i][self.y+j],end=" ")
                print()       
    def next_y(self):
        if self.y+len(self.p[0])<len(self.grid[0]):
            for i in range(len(self.p)):
                self.current -= self.grid[self.x+i][self.y]
                self.current += self.grid[self.x+i][self.y+len(self.p[0])]
            self.y+=1
        # else:
        #     self.done = True



x=Grid([[1,2,1,1,2,1],
        [1,2,1,1,2,1],
        [1,2,1,1,2,1],
        [1,3,1,1,2,1]],[[1,2,1],[1,2,1],[1,2,1]])
print(x.match())
x.draw()
x.next()
print(x.match())
x.draw()
x.next()
print(x.match())
x.draw()
x.next()
print(x.match())
x.draw()
x.next()
print(x.match())
x.draw()
x.next()
print(x.match())
x.draw()
x.next()
print(x.match())
x.draw()
x.next()
print(x.match())
x.draw()
x.next()
print(x.match())
x.draw()
x.next()
print(x.match())
x.draw()
x.next()
print(x.match())
x.draw()
x.next()
print(x.match())
x.draw()
print(x.count)
print(x.where)