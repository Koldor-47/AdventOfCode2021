
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
                the_row.append(0)
            the_grid.append(the_row)

        return the_grid

    def print(self):
        for row in self.grid:
            for col in row:
                print(col, end="")
            print()
    
    def markLine2(self, aVentLine):
        self.xDiff = aVentLine.begin[0] - aVentLine.end[0]
        self.yDiff = aVentLine.begin[1] - aVentLine.end[1]
        self.currentX = aVentLine.begin[0] 
        self.currentY = aVentLine.begin[1] 
        xchange = 0
        ychange = 0 
        if self.xDiff > 0:
            xchange = -1
        else:
            xchange = 1
        if self.yDiff > 0:
            ychange = -1
        else:
            ychange = 1
        
        self.check_spot(self.currentY, self.currentX)

        while True:
            
            if self.currentX != aVentLine.end[0]:
                self.currentX += xchange
            if self.currentY != aVentLine.end[1]:
                self.currentY += ychange
            self.check_spot(self.currentY, self.currentX)
            if self.currentX == aVentLine.end[0] and self.currentY == aVentLine.end[1]:
                break

    def check_spot(self, y, x):
        if self.grid[y][x] < 1:
            self.grid[y][x] = 1
        else:
            self.grid[y][x] += 1       



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

    def OverLap(self):
        count = 0
        for row in self.grid:
            for col in row:
                if col > 1:
                    count += 1
        return count
def get_data(filePath):
    with open(filePath, 'r') as openFile:
        data = openFile.read()

    return data



readData = get_data(r"C:\Users\nickk\Documents\Code\Python\AdventOfCode2021\AdventOfCode2021\day5\day5.txt")
readTest = [x.split(" -> ") for x in readData.split("\n")]
lines = []

for corrod in readTest:
    beg = tuple([int(x) for x in corrod[0].split(',')])
    end = tuple([int(x) for x in corrod[1].split(',')])
    x = ventLines(beg, end)
    lines.append(x)    

test = ventLines((9, 7),(7, 9))

x = oceanFloor(1000)
for line in lines:
    x.markLine2(line)
print(f" Overlapping lines = {x.OverLap()}")

