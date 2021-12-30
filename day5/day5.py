
from os import read


class ventLines:
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end


def get_data(filePath):
    with open(filePath, 'r') as openFile:
        data = openFile.read()

    return data

def grid(size):
    the_grid = []
    for row in range(size):
        the_row = []
        for col in range(size):
            the_row.append('.')
        the_grid.append(the_row)

    return the_grid

readData = get_data(r"C:\Users\nickk\Documents\Code\Python\AdventOfCode2021\day5Data.txt")
readTest = [x.split(" -> ") for x in readData.split("\n")]
lines = []

for corrod in readTest:
    beg = tuple([int(x) for x in corrod[0].split(',')])
    end = tuple([int(x) for x in corrod[1].split(',')])
    x = ventLines(beg, end)
    lines.append(x)    

small_grid = grid(10)

small_grid[0][6] = 'X'

for t in small_grid:
    print(t)