import numpy as np

debug = False

# %% Load and parse
if debug:
    with open('Day11.example','r') as f:
        data = f.read().splitlines()
else:
    with open('Day11.input','r') as f:
        data = f.read().splitlines()
        
seats = np.empty([len(data), len(data[0])], dtype = str)
for idx, line in enumerate(data):
    for jdx, char in enumerate(line):
        seats[idx,jdx] = char

# %% Count neighbors
def countNeighbors(row, col):
    count = 0
    # Previous Row
    if row-1 >= 0:
        if col -1 >= 0:
            # print('Row: {} Col: {}'.format(row-1, col-1))
            if seats[row-1, col-1] =='#':
                count += 1
        if col + 1 <= len(seats[0])-1:
            # print('Row: {} Col: {}'.format(row-1, col+1))
            if seats[row-1, col+1] == '#':
                count += 1
        if seats[row-1, col] == '#':
            # print('Row: {} Col: {}'.format(row-1, col))
            count += 1
    # Next Row
    if row + 1 <= len(seats)-1:
        if col - 1 >= 0:
            if seats[row+1, col-1] =='#':
                count += 1
        if col + 1 <= len(seats[0])-1:
            if seats[row+1, col+1] == '#':
                count += 1
        if seats[row+1, col] == '#':
            count += 1
    # This Row
    if col - 1 >= 0:
        if seats[row, col-1] =='#':
            count += 1
    if col + 1 <= len(seats[0])-1:
        if seats[row, col+1] == '#':
            count += 1
    return count

# %% Next Generation
def nextStep(row,col):
    n = countNeighbors(row,col)
    if seats[row, col] == 'L':  # If seat unoccupied
        if n == 0:
            nextGen = '#'
        else:
            nextGen = 'L'
    elif seats[row,col] == '#': # If seat occupied
        if n >= 4:
            nextGen = 'L'
        else: 
            nextGen = '#'
    else:
        nextGen = seats[row, col]
    return nextGen

# %% Next Gen's map
def calcNextGen():
    nextMap = np.empty([len(data),len(data[0])],dtype='str')
    for row in range(len(seats)):
        for col in range(len(seats[0])):
            nextMap[row, col] = nextStep(row, col)
    return nextMap

# %% Count seats
def countOccupied(inGen):
    count = 0
    for i in inGen:
        for j in i:
            if j == '#':
                count += 1
    return count

# %% Run n generations
def runIt(n):
    global seats
    while True:
        if n <= 0:
            break
        seats = calcNextGen()
        n -= 1
    return seats

# %% Find when it stablizes

while True:
    print(countOccupied(seats))
    seats = runIt(1)