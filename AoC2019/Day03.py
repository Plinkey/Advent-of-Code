

""" Find intersections in some way

record a list of every vertex the wires pass through. Don't need to plot,
just need a list of every point the wires go through"""

A,B,_ = open('Day03.input').read().split('\n')
A,B = [x.split(',') for x in [A,B]]

moveX = {'L': -1, 'R': 1, 'U': 0, 'D': 0}
moveY = {'L': 0, 'R': 0, 'U': 1, 'D': -1}
 
def plotWire(A):
    x = 0
    y = 0
    length = 0
    ans = {}
    for cmd in A:
        # d direction
        direction = cmd[0]
        # n number of moves
        nMoves = int(cmd[1:])
        # for each step, move in the direction and count length
        for i in range(nMoves):
            x += moveX[direction]
            y += moveY[direction]
            length += 1
            # record position as a location for the wire in a list
            if (x,y) not in ans:
                # Length needed for part 2
                ans[(x,y)] = length
    return ans

# Plot wire A
PA = plotWire(A)

# Plot wire B
PB = plotWire(B)

# Find intersection from the subreddit for syntax on this step
both = set(PA.keys())&set(PB.keys())

# Find the minimum taxicab distance


answer_part1 = min([abs(x)+abs(y) for (x,y) in both])
print ("Part 1 answer: "+str(answer_part1))


answer_part2 = min([PA[p] + PB[p] for p in both])
print("Part 2 answer: " + str(answer_part2))

