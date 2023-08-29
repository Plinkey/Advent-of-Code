""" Advent of Code 2018 Day10
I am not a computer programmer
Got a lot of help from /r/adventofcode"""

with open('Inputs\Day10.input', 'r') as f:
    rawData = f.read().splitlines()


# Parse
lines = [line.replace("<","[").replace(">","]")[9:] for line in rawData]
pts_vels = [map(eval,line.split(" velocity=")) for line in lines]

points,velocities = zip(*pts_vels)
# Well holy shit. zip is a nice function I've never seen before

# Find minimum bound box.  when the points align
# into text, the bounding box will be minimized
def boundBox(inp):
    return map(min,inp),map(max,inp)

def printpts(points):
    (xmin,ymin),(xmax,ymax) = boundBox(zip(*points))
    for y in xrange(ymin,ymax+1):
        line=""
        for x in xrange(xmin,xmax+1):
            if [x,y] in points:
                line+="#"
            else:
                line+=" "
        print line

def add(v1,v2):
    return [a+b for a,b in zip(v1,v2)]

ytol = 15   # tolerance for height of text
s = 0       # seconds to wait Part 2




while True:
    (xmin,ymin),(xmax,ymax) = boundBox(zip(*points))
    if abs(ymax-ymin) < ytol:
        break
    points = [add(pt,v) for pt,v in zip(points,velocities)]
    s+=1 # adding this for part 2

# originally, I had a larger height tolerance (100)
# and printed in another while loop here.


printpts(points)    # part 1

##################
# Part 2
##################

print s             # part 2
