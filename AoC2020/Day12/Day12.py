from collections import deque
# %% 
# with open('Day12.example','r') as f:
#     data = f.read().splitlines()
    
# %%
with open('Day12.input', 'r') as f:
    data = f.read().splitlines()
    
# %% return direction, distance
def readStr(instr):
    direction = instr[0]
    distance = int(instr[1:])
    return direction, distance

# %%
"""Action N means to move north by the given value.
Action S means to move south by the given value.
Action E means to move east by the given value.
Action W means to move west by the given value.
Action L means to turn left the given number of degrees.
Action R means to turn right the given number of degrees.
Action F means to move forward by the given value in the direction the ship is currently facing.
"""
coord = [0,0]
directions = ['E','S','W','N']
directions = deque(directions)
# Deque.rotate -ve moves clockwise
# Deque.rotate +ve moves ccw

# %% Move
def process(instr):
    a, b = readStr(instr)
    if a in ['L','R']:
        turn(instr)
    elif a == 'F':
        move(directions[0],b)
    else:
        move(a,b)
    
# %% Turn    
def turn(instr):
    global directions
    a, b = readStr(instr)
    if a == 'L': # Turn Left by degrees
        directions.rotate(b//90)
    elif a == 'R': # Turn right by degrees
        directions.rotate(-b//90)

# %% Move      
def move(a, b):
    global coord
    if a == 'N': # Move North (+ve)
        coord[0] += b
    elif a == 'S': # Move South (-ve)
        coord[0] -= b
    elif a == 'E': # Move East (+ve)
        coord[1] += b
    elif a == 'W': # Move West (-ve)
        coord[1] -= b

# %% RunIt
for d in data:
    process(d)
print('The answer to part one is: {}'.format(abs(coord[0])+abs(coord[1])))
    
# %% initialize part2
            
ship = [0, 0]
coord = [1, 10]

# %% process2
def process2(instr):
    global ship
    global coord
    a, b = readStr(instr)
    if a == 'F':
        ship = moveship(b)
    elif a in ['L','R']:
        rotWaypoint(a,b)
    else:
        move(a,b)
# %% moveship
def moveship(b):
    global ship
    ship[0] = ship[0] + b * coord[0]
    ship[1] = ship[1] +  b * coord[1]
    return ship
    
# %% def rotWaypoint
def rotWaypoint(a,b):
    global coord
    tmp = [0,0]
    if a == 'R':
        sign = 1
    if a == 'L':
        sign = -1
    if b == 180:
        tmp[0] =  -coord[0]
        tmp[1] =  -coord[1]
    if b == 90:
        tmp[0] = sign * -coord[1]
        tmp[1] = sign * coord[0]
    if b == 270:
        tmp[0] = sign * coord[1]
        tmp[1] = sign * -coord[0]
    coord = tmp


# %% RnIt2

for d in data:
    process2(d)
print('The answer to part two is: {}'.format(abs(ship[0])+abs(ship[1])))

# 7957 too low



























  