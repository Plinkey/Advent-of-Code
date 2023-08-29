# Day10
# Test inputs:
# Test1 == asteroid at 3,4 w/ 8
# Test2 == asteroid at 5,8 w/ 33
# Test3 == asteroid at 1,2 w/ 35
# Test4 == asteroid at 6,3 w/ 41
# Test5 == asteroid at 11,13 w/ 210

import numpy as np
import math
import fractions
with open('Day10\Day10.input','r') as f:
    data = np.array([list(line.strip()) for line in f]) == '#'

#data = np.swapaxes(data,0,1) # Swap coordinates from(y,x) to (x,y)
    
def slope(base,target):
    x1, y1 = base
    x2, y2 = target
    a = y2-y1
    b = x2-x1
    # Alright, this is going to get weird.
    # if looking LEFT AND UP, 9000 + slope a&b < 0 QUAD I
    # if looking RIGHT AND UP, 8000 + slope a < 0, b >0
    # if looking LEFT AND DOWN, 7000 + slope a>0, b<0
    # if looking RIGHT AND DOWN, 6000 + slope a>0, b< 0
    if a < 0:
        if b < 0: #Looking left and up
            return 9000 + fractions.Fraction(a,b)
        elif b > 0: # looking RIGHT and UP
            return 8000 + fractions.Fraction(a,b)
        else: # b == 0
            return -180
    elif a > 0:
        if b<0: #looking LEFT and DOWN
            return 7000 + fractions.Fraction(a,b)
        elif b>0:
            return 6000 + fractions.Fraction(a,b)
        else: # b == 0
            return +1980
    else: # a == 0
        if b > 0:
            return +999
        else:
            return -999
            
slopesCurAsteroid = []
allAsteroids = []    

locAsteroids = [np.array(point) for point in zip(*np.nonzero(data))] #location of all asteroids

for x in locAsteroids:
    for y in locAsteroids:
        if np.array_equal(x,y):
            continue
        else:
            curSlope = slope(x,y)
            if curSlope not in slopesCurAsteroid:
                slopesCurAsteroid.append(curSlope)
    allAsteroids.append(len(slopesCurAsteroid))
    slopesCurAsteroid = []                
                
max(allAsteroids)


