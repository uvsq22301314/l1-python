from random import randint

class Cell:
    def __init__(self, value = None):
        self.value = value

class Grid:
    def __init__(self):
        self.grid = [[Cell() for __ in range(4)] for _ in range(4)]
    

    def print_grid(self):
        print("\n\n")
        for i in range(4):
            print([self.grid[i][j].value for j in range(4)])

    def add_Num(self):
        nb = 2 if randint(0, 1) < 0.9 else 4
        
        possibilities = [(i%4, i//4) for i in range(16) if self.grid[i%4][i//4].value is None]
        coord = possibilities[randint(0, len(possibilities))]

        self.grid[coord[0]][coord[1]].value = nb

    def findNearestNone(self, dir, line_list, coordY):
        op = [1, -1][dir]
        re = [3, 0][dir]
        
        
        if coordY == re or line_list[coordY + op].value is not None:
            return False
        else:
            index = coordY + op
            while index != 3 and line_list[index].value is None :
                index += op
                
            return index

    def depl(self, dir):
        cond = dir < 2
        d = dir%2 # Direction
        for i in range(4):
            arg = self.grid[i] if cond else [self.grid[j][i] for j in range(4)]

            for j in range(4):
                res = self.findNearestNone(d, arg, j)
                if not res: 
                    continue

                if arg[j].value == arg[res].value:
                    arg[j].value = None
                    arg[res].value *= 2
                else:
                    arg[res] = arg[j].value
                    arg[j].value = None
                

"""
continue si pas de None+1
Tant que None avancer (dro, gau, hau, bas) 
Si valeur == None +1
	None+1 *= 2
Sinon :	
	None = case
""" 


g = Grid()
g.grid[1][0].value = 2
print(g.findNearestNone(1, [g.grid[i][0] for i in range(4)], 3))