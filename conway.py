# Write your code here :-)
import random, time, copy
WIDTH = 60
HEIGHT = 20

next_cells = []
for x in range(WIDTH):
    column = []
    for y in range(HEIGHT):
        if random.randint(0, 2) == 0:
            column.append('#')
        else:
            column.append(' ')
    next_cells.append(column)

while True:
    print('\n\n\n\n\n')
    current_cells = copy.deepcopy(next_cells)

for y in range(HEIGHT):
    for x in range(WIDTH):
        print(current_cells[x][y], end='')
    print()

for x in range(WIDTH):
    for y in range(HEIGHT):
        leftCoord = (x-1) % WIDTH
        rightCoord = (x+1) % WIDTH
        aboveCoord = (y-1) % HEIGHT
        belowCoord = (y+1) % HEIGHT

        numNeighbors = 0
        if current_cells[leftCoord][aboveCoord] == '#':
            numNeighbors += 1
        if current_cells[x][aboveCoord] == '#':
            numNeighbors += 1
        if current_cells[rightCoord][aboveCoord] == '#':
            numNeighbors += 1
        if current_cells[leftCoord][y] == '#':
            numNeighbors += 1
        if current_cells[rightCoord][y] == '#':
            numNeighbors += 1
        if current_cells[leftCoord][belowCoord] == '#':
            numNeighbors += 1
        if current_cells[x][belowCoord] == '#':
            numNeighbors += 1
        if current_cells[rightCoord][belowCoord] == '#':
            numNeighbors += 1

        if current_cells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
            next_cells[x][y] = '#'
        elif current_cells[x][y] == ' ' and numNeighbors == 3:
            next_cells[x][y] = '#'
        else:
            next_cells[x][y] = ' '
time.sleep(1)

