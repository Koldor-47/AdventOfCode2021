
from os import read


class ventLines:
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end


class oceanFloor:

    def __init__(self, sizeOfGrid):
        self.grid = self.Makegrid(sizeOfGrid)


    def Makegrid(self, size):
        the_grid = []
        for row in range(size):
            the_row = []
            for col in range(size):
                the_row.append('.')
            the_grid.append(the_row)

        return the_grid

    def print(self):
        for row in self.grid:
            for col in row:
                print(col, end="")
            print()
    
    def markLine(self, VentLine):
        self.x1, self.y1 = VentLine.begin[0], VentLine.begin[1]
        self.x2, self.y2 = VentLine.end[0], VentLine.end[1]
        self.xDiff = abs(self.x1 - self.x2)
        self.yDiff = abs(self.y1 - self.y2)
        if self.yDiff == 0:
            if self.x1 < self.x2:
                for i in range(self.x1, (self.x2 +1)):
                    if self.grid[self.y1][i] == '.':
                        self.grid[self.y1][i] = 1
                    else:
                        self.grid[self.y1][i] += 1
            else:
                for i in range(self.x2, (self.x1 + 1)):
                    if self.grid[self.y1][i] == '.':
                        self.grid[self.y1][i] = 1
                    else:
                        self.grid[self.y1][i] += 1
        
        if self.xDiff == 0:
            if self.y1 < self.y2:
                for i in range(self.y1, (self.y2 + 1)):
                    if self.grid[i][self.x1] == '.':
                        self.grid[i][self.x1] = 1
                    else:
                        self.grid[i][self.x1] += 1
            else:
                for i in range(self.y2, (self.y1 +1)):
                    if self.grid[i][self.x1] == '.':
                        self.grid[i][self.x1] = 1
                    else:
                        self.grid[i][self.x1] += 1


def get_data(filePath):
    with open(filePath, 'r') as openFile:
        data = openFile.read()

    return data



readData = get_data(r"C:\Users\nickk\Documents\Code\Python\AdventOfCode2021\AdventOfCode2021\day5\day5Data.txt")
readTest = [x.split(" -> ") for x in readData.split("\n")]
lines = []

for corrod in readTest:
    beg = tuple([int(x) for x in corrod[0].split(',')])
    end = tuple([int(x) for x in corrod[1].split(',')])
    x = ventLines(beg, end)
    lines.append(x)    


x = oceanFloor(10)
for i in lines:
    x.markLine(i)
x.print()