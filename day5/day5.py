
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

x.print()