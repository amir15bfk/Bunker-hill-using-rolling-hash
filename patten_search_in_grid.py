class Grid():
    def __init__(self,grid):
        self.grid = grid
    def hash(self,x):
        return sum(sum(x[i][j] for i in range(len(self.p))) for j in range(len(self.p[0])))
    def __match(self):
        if self.current == self.hp:
            #TODO : real check of equality
            for i in range(len(self.p)):
                for j in range(len(self.p[0])):
                    if self.grid[self.x+i][self.y+j]!=self.p[i][j]:
                        return False

            if 1:
                self.count += 1 
                self.where.append((self.x,self.y))
                return True
        else:
            return False
    def __next(self):
        if not self.done:
            if (self.mw == 1 and (self.x+len(self.p))==len(self.grid))or(self.mw == -1 and (self.x==0)):
                self.__next_y()
                self.mw*=-1 
            else:
                if self.mw == 1:
                    if ((self.x+len(self.p))<len(self.grid)):
                        for i in range(len(self.p[0])):
                            self.current -= self.grid[self.x][self.y+i]
                            self.current += self.grid[self.x+len(self.p)][self.y+i]
                else:
                    if (0<self.x):
                        for i in range(len(self.p[0])):
                            self.current += self.grid[self.x-1][self.y+i]
                            self.current -= self.grid[self.x+len(self.p)-1][self.y+i]
            
                self.x+=self.mw
                
    def draw(self):
        for i in range(len(self.p)):
                for j in range(len(self.p[0])):
                    print(self.grid[self.x+i][self.y+j],end=" ")
                print()       
    def __next_y(self):
        if self.y+len(self.p[0])<len(self.grid[0]):
            for i in range(len(self.p)):
                self.current -= self.grid[self.x+i][self.y]
                self.current += self.grid[self.x+i][self.y+len(self.p[0])]
            self.y+=1
        else:
            self.done = True
    def run(self,p):
        self.p = p
        self.x = 0
        self.y = 0
        self.mw = 1
        self.current = self.hash(self.grid)
        self.hp = self.hash(self.p)
        self.done = False
        self.count = 0 
        self.where = []
        while not self.done:
            self.__match()
            self.__next()
        return self.count,self.where



x=Grid([[1,2,1,1,2,1],
        [1,2,1,1,2,1],
        [1,2,1,1,2,1],
        [1,3,1,1,2,1],
        [1,2,1,1,2,1],
        [1,2,1,1,2,1],
        [1,2,1,1,2,1],
        [1,3,1,1,2,1],
        [1,2,1,1,2,1],
        [1,2,1,1,2,1],
        [1,2,1,1,2,1],
        [1,3,1,1,2,1],
        [1,2,1,1,2,1],
        [1,2,1,1,2,1],
        [1,2,1,1,2,1],
        [1,3,1,1,2,1],
        [1,2,1,1,2,1],
        [1,2,1,1,2,1],
        [1,2,1,1,2,1],
        [1,3,1,1,2,1],
        [1,2,1,1,2,1],
        [1,2,1,1,2,1],
        [1,2,1,1,2,1],
        [1,3,1,1,2,1],
        [1,2,1,1,2,1],
        [1,2,1,1,2,1],
        [1,2,1,1,2,1],
        [1,3,1,1,2,1]])
p = [[2,1,1,2],[2,1,1,2],[2,1,1,2]] 
c,w= x.run(p)
print(c)
print(w)