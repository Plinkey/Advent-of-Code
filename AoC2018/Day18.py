""" Advent of Code Day 18


NOTES:
    lumber area is 50 x 50
    . ground
    | trees
    # lumberyard
    scan of the area is puzzle input

    looks at surrounding 8 NW N NE
                            W    E
                           SW S SE
    
    if 3 or more are |:
        . -> |
    else:
        nothing

    if nSurroundTrees >= 3:
        . becomes |
    else:
        nothing

#########################
    if 3 or more are #
        | -> #
    else:
        nothing

    if nsurroundLumber >= 3:
        | becomes #
    else:
        nothing


#########################
    if 1 or more are # AND 1 or more |:
        # remains
    else:
        # -> . 


    if nSurroundLumber >= 1 AND nSurroundTrees >= 1:
        nothing
    else:
        # becomes .

    everything happens simultaneouslys

"""
import numpy as np

#with open('Inputs\Day18TEST.input', 'r') as f:
with open('Inputs\Day18.input', 'r') as f:
    rawData = f.read().splitlines()

Map = np.zeros([len(rawData), len(rawData[0])], 'str')
for idx, line in enumerate(rawData):
    for jdx, value in enumerate(line):
        Map[idx, jdx] = value 

#print Map


##################
# Helper functions
##################

def GetSurround(ydx,xdx):
    yLen, xLen = Map.shape 
    # NORTHWEST
    if ydx > 0 and xdx > 0:
        NW = Map[(ydx-1, xdx-1)]
    else:
        NW = ' '

    # NORTH
    if ydx > 0:
        N  = Map[(ydx-1, xdx)]
    else:
        N = ' '

    # NORTHEAST
    if ydx > 0 and xdx < xLen-1:
        NE = Map[(ydx-1, xdx+1)]
    else:
        NE = ' '

    # WEST
    if xdx > 0:
        W  = Map[(ydx, xdx-1)]
    else:
        W = ' '

    # EAST
    if xdx < xLen-1:
        E  = Map[(ydx, xdx+1)]
    else:
        E = ' '


    # SOUTHWEST
    if ydx < yLen-1 and xdx > 0:
        SW = Map[(ydx+1, xdx-1)]
    else:
        SW = ' '

    #SOUTH
    if ydx < yLen-1:
        S  = Map[(ydx+1, xdx)]
    else:
        S = ' '

    # SOOUTHEAST
    if ydx < yLen-1 and xdx < xLen-1:
        SE = Map[(ydx+1, xdx+1)]
    else:
        SE = ' '
    return [NW, N, NE, W, E, SW, S, SE]

#print 'Testing GetSurround with Day18TEST.input'
#print 'The line below should equal [\' \', \' \', \' \', \' \', \'#\', \' \', \'.\', \'.\']'
#print GetSurround(0,0)


def CountTrees(idx, jdx):
    surround = GetSurround(idx, jdx)
    return surround.count('|')

#print "Testing CountTrees with Day18TEST.input"
#print "The line below should = 0"
#print CountTrees(0,0)
#print ''
#print 'The line below should = 2'
#print CountTrees(3,1)

def CountLumber(idx, jdx):
    surround = GetSurround(idx, jdx)
    return surround.count('#')

#print "Testing CountLumber with Day18TEST.input"
#print "The line below should = 1"
#print CountLumber(0,0)
#print ''
#print 'The line below should = 2'
#print CountLumber(0,2)
#print ''
#print 'The line below should = 2'
#print CountLumber(5,1)

def EmptyLandTest(ydx, xdx):
    """
    if 3 or more are |:
        . -> |
    else:
        nothing

    if nSurroundTrees >= 3:
        . becomes |
    else:
        nothing
        """
    if Map[(ydx, xdx)] != '.': #oops, wrong input
        return Map[(ydx, xdx)]
    else:
        nTrees = CountTrees(ydx, xdx)
        if nTrees >= 3:
            return '|'
        else:
            return '.'

#print 'Testing EmptyLandTest with Day18TEST.input'
#print "The line below should = \'.\'"
#print EmptyLandTest(0,0)
#print ''
#print 'The line below should = |'
#print EmptyLandTest(5,4)

def TreeLandTest(ydx, xdx):
    """
    if 3 or more are #
        | -> #
    else:
        nothing

    if nsurroundLumber >= 3:
        | becomes #
    else:
        nothing
        """
    if Map[(ydx, xdx)] != '|': #oops, wrong input
        return Map[(ydx, xdx)]
    else:
        nLumber = CountLumber(ydx, xdx)
        if nLumber >= 3:
            return '#'
        else:
            return '|'

#print 'Testing TreeLandTest with Day18TEST.input'
#print "The line below should = \'.\'"
#print TreeLandTest(0,1)
#print ''
#print 'The line below should = #'
#print TreeLandTest(0,7)

def LumberLandTest(ydx, xdx):
    """
    if 1 or more are # AND 1 or more |:
        # remains
    else:
        # -> . 


    if nSurroundLumber >= 1 AND nSurroundTrees >= 1:
        nothing
    else:
        # becomes .
        """
    if Map[(ydx, xdx)] != '#': # oops, wrong input
        return Map[(ydx, xdx)]
    else:
        nTrees = CountTrees(ydx,xdx)
        nLumber = CountLumber(ydx,xdx)
        if nTrees >= 1 and nLumber >= 1:
            return '#' # nothing changes
        else:
            return '.' # changes to empty
#print 'Testing LumberLandTest with Day18TEST.input'
#print "The line below should = #"
#print LumberLandTest(0,8)
#print ''
#print 'The line below should = .'
#print LumberLandTest(0,1)

def NextGen(ydx, xdx):
    if Map[(ydx, xdx)] == '.':
        char = EmptyLandTest(ydx, xdx) 
    elif Map[(ydx, xdx)] == '|':
        char = TreeLandTest(ydx, xdx)
    elif Map[(ydx, xdx)] == '#':
        char = LumberLandTest(ydx, xdx)
    else:
        print "Crap! Wrong Map input"
    return char

def PrintMap(inMap):
    for i in inMap:
        print ''.join(i)

NewMap = Map.copy()
t = 0 #time = 0 mins
#while t < 10:
while t < 1000000000:
#while t < 2:
    t += 1
    for ydx in range(len(Map)):
        for xdx in range(len(Map[0])):
            NewMap[(ydx, xdx)] = NextGen(ydx, xdx)
    #print "After ", t, "mins"
    #PrintMap(NewMap)
    #print "\n"
    Map = NewMap.copy()
    nTrees = 0
    nLumber = 0 
    for ydx in range(len(Map)):
        for xdx in range(len(Map[0])):
            if Map[(ydx, xdx)] == '|':
                nTrees += 1
            elif Map[(ydx, xdx)] == '#':
                nLumber += 1
    nTrees = 0
    nLumber = 0 
    for ydx in range(len(Map)):
        for xdx in range(len(Map[0])):
            if Map[(ydx, xdx)] == '|':
                nTrees += 1
            elif Map[(ydx, xdx)] == '#':
                nLumber += 1
    print "Minutes: ", t, "Resource", nTrees*nLumber

"""
nTrees = 0
nLumber = 0 
for ydx in range(len(Map)):
    for xdx in range(len(Map[0])):
        if Map[(ydx, xdx)] == '|':
            nTrees += 1
        elif Map[(ydx, xdx)] == '#':
            nLumber += 1

#PrintMap(Map)
answer = nTrees * nLumber
print "nTrees = ", nTrees
print "nLumber = ", nLumber
print "answer = ", answer 
"""


# Periodic w/ period 28
# 2700
"""

Minutes:	3000	Resource	176900
Minutes:	3001	Resource	183084
Minutes:	3002	Resource	189630
Minutes:	3003	Resource	197938
Minutes:	3004	Resource	205737
Minutes:	3005	Resource	216216
Minutes:	3006	Resource	215877
Minutes:	3007	Resource	215096
Minutes:	3008	Resource	215160
Minutes:	3009	Resource	217728
Minutes:	3010	Resource	217672
Minutes:	3011	Resource	219726
Minutes:	3012	Resource	214878
Minutes:	3013	Resource	189088
Minutes:	3014	Resource	191540
Minutes:	3015	Resource	199593
Minutes:	3016	Resource	199064
Minutes:	3017	Resource	199283
Minutes:	3018	Resource	186550
Minutes:	3019	Resource	182252
Minutes:	3020	Resource	176468
Minutes:	3021	Resource	174028
Minutes:	3022	Resource	170016
Minutes:	3023	Resource	167445
Minutes:	3024	Resource	161214
Minutes:	3025	Resource	164666
Minutes:	3026	Resource	165599
Minutes:	3027	Resource	171970


SO Take (nGeneration - 3000) % 28 and look it up on the list above
