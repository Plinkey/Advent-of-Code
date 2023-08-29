""" Advent of Code Day 13"""
import numpy as np
import copy

# Below should colide at (7,3)
#with open('Inputs\Day13TEST.input','r') as f:
    #rawData = f.read().splitlines()

# Below should colide at (0,2)
#with open('inputs\day13test1.input','r') as f:
    #rawData = f.read().splitlines()

# Below should colide at (2,0)
#with open('inputs\day13test2.input','r') as f:
    #rawData = f.read().splitlines()

# Below should colide at (1,0)
#with open('inputs\day13test3.input','r') as f:
    #rawData = f.read().splitlines()

with open('Inputs\Day13.input','r') as f:
    rawData = f.read().splitlines()

#
#
#
#
#  NOTE TO MYSELF: X is LEFT AND RIGHT +ve RIGHT
#                  Y is UP AND DOWN    +ve DOWN
#
#
#



############
#  Helper Functions/Classes
############

def PrintMap(Map, carts):
    tempMap = copy.deepcopy(Map)
    if carts:
        for i in carts:
            y,x,char = i.PlotCart()
            #print y, x, char
            tempMap[y][x] = char
    for i in tempMap:
        print ''.join(i)


def CheckCollision(cart1, cart2):
    if cart1.curX == cart2.curX and cart1.curY == cart2.curY:
        return True
    else:
        return False

def FindNextCartToMove(Carts):
    #print "runningFindNExtCartToMove"
    global tick
    curMinX = mapSizeX
    curMinY = mapSizeY
    idxOfCart = -1
    for num, cart in enumerate(Carts):
        if cart.curY <= curMinY:
            if cart.curX <= curMinX:
                if cart.lastMoved <= tick:
                    #print "idxOfCart = ", num
                    #print "curMinX = ", cart.curX
                    #print "curMinY =", cart.curY
                    idxOfCart = num
                    curMinX = cart.curX
                    curMinY = cart.curY
    if idxOfCart != -1:
        #print "CART FOUND to move", idxOfCart, curMinX, curMinY
        #print listCarts[idxOfCart].lastMoved 
        #print "new updated lastmoved = ", listCarts[idxOfCart].lastMoved
        return idxOfCart
    else:
        #print "ALL CARTS DONE THIS TICK!"
        tick += 1
        return False

def MoveNextCart():
    nextCart = FindNextCartToMove(listCarts)
    listCarts[nextCart].lastMoved += 1
    listCarts[nextCart].MoveCart()

def CheckAllCollision():
    collisionFlag = False
    rcart1 = -1 # flag meaning no cart found
    rcart2 = -1
    for i, cart1 in enumerate(listCarts):
        for j, cart2 in enumerate(listCarts):
            if i == j:
                continue
            else:
                collisionFlag = CheckCollision(cart1, cart2)
                rcart1 = cart1
                rcart2 = cart2
    return collisionFlag, rcart1, rcart2

def PrintCollision(cart1, cart2):
    print cart1.curX, cart1.curY
    print cart2.curX, cart2.curY

class Cart:
    def __init__(self, initY, initX, char):
    #def __init__(self,char, initX, initY):
        # Position
        self.curX = initX
        self.curY = initY
        #print "Made a cart at", self.curY, self.curX
        # Pointing
        if char == '<': # pointing left
            self.curPoint = 'Left'
        elif char == '^': # pointing Up
            self.curPoint = 'Up'
        elif char == '>': # pointing Right
            self.curPoint = 'Right'
        elif char == 'v': # pointing Down
            self.curPoint = 'Down'
        else:
            print "Shit. Something broke when determining initial pointing"
        self.turns = ['Left','Straight','Right']
        self.lastMoved = 0

    def MoveCart(self):
        # Move
        if self.curPoint == 'Left':
            self.curX -= 1
        elif self.curPoint == 'Right':
            self.curX += 1
        elif self.curPoint == 'Up':
            self.curY -= 1
        elif self.curPoint == 'Down':
            self.curY += 1
        # Check for Intersection
        if CartMap[self.curY][self.curX] == '+':
            self.EncounterIntersection()
        # Check for Track Turn
        elif CartMap[self.curY][self.curX] in ['/','\\']:
            self.EncounterTurn()

    
    def WhichWay(self):
        # When encountering an intersection, returns which way the cart should go
        answer = self.turns[0]
        self.turns = self.turns[1:] + self.turns[:1]
        return answer

    def EncounterIntersection(self):
        # When cart lands on intersection, it'll first turn left, then straight, then right
        # This all happens instantly, the next turn it will move the next spot in that dir
        #self.TurnCart(self.WhichWay())
        ans = self.WhichWay()
        #print "Turning = ", ans
        self.TurnCart(ans)

    def EncounterTurn(self):
        # When cart lands on turn in the track, turn the cart in that direction 
        trackPiece = CartMap[self.curY][self.curX]
        if trackPiece == '/': # left turn or right turn, depending on direction
            if self.curPoint == 'Left': # then you're turning Left
                self.TurnCart('Left')
            elif self.curPoint == 'Up': # then you're turning RIGHT
                self.TurnCart('Right')
            elif self.curPoint == 'Right': # then you're turning LEFT
                self.TurnCart('Left')
            elif self.curPoint == 'Down': # then you're turning RIGHT
                self.TurnCart('Right')
        elif trackPiece == '\\':
            if self.curPoint == 'Left': # then you're turning Left
                self.TurnCart('Right')
            elif self.curPoint == 'Up': # then you're turning RIGHT
                self.TurnCart('Left')
            elif self.curPoint == 'Right': # then you're turning LEFT
                self.TurnCart('Right')
            elif self.curPoint == 'Down': # then you're turning RIGHT
                self.TurnCart('Left')

    def TurnCart(self, turn):
        turns = ['Left','Down','Right','Up']
        #leftTurns = ['Left','Down','Right','Up']
        #rightTurns = ['Left','Up','Right','Down']
        if turn == 'Straight':
            self.curPoint = self.curPoint
        elif turn == 'Right': # ROT through turns back one pos 
            idx = turns.index(self.curPoint)
            if idx >= 1: # don't worry about wraparound
                self.curPoint =  turns[idx-1]
            else: # wraparound
                self.curPoint = turns[-1]
        elif turn == 'Left': # ROT through turns fwd oen pos
            idx = turns.index(self.curPoint)
            if idx < len(turns)-1: # don't worry about wrap
                self.curPoint = turns[idx+1]
            else: # wrap
                self.curPoint =  turns[0]

    def PlotCart(self):
        if self.curPoint == 'Left':
            pointChar = '<'
        if self.curPoint == 'Right':
            pointChar = '>'
        if self.curPoint == 'Up':
            pointChar = '^'
        if self.curPoint == 'Down':
            pointChar = 'v'
        return self.curY, self.curX, pointChar








############
#  Initialize
############



mapSizeY = len(rawData)
mapSizeX = len(rawData[0])


# Seed empty CartMap of correct size.  Spaces represent nothing
# Will fill in map with cart lines in separate process
CartMap = np.full([mapSizeY, mapSizeX], ' ',dtype=str)

listCarts = []

collisionFlag = False
tick = 0

############
#  Read Map, Create Cart
############

# Fill in Cart Map
for ydx, line in enumerate(rawData): # for each line in rawData
    for xdx, char in enumerate(line): #for each character in line 
        if char not in ['<','>','^','v']: # will handle track under carts differently
            CartMap[ydx][xdx] = char
        elif char in ['<','>']: # replace with horizontal track
            CartMap[ydx][xdx] = '-'
            #print "Found a cart at", ydx, xdx
            listCarts.append(Cart(ydx, xdx, char))
        elif char in ['^','v']: # replace with vertical track
            CartMap[ydx][xdx] = '|'
            #print "Found a cart at", ydx, xdx
            listCarts.append(Cart(ydx, xdx, char))
        else:
            print "Shit. Something Broke when reading MAP."

#PrintMap(CartMap,[])
#print listCarts
#PrintMap(CartMap, listCarts)


while not collisionFlag:
    MoveNextCart()
    #PrintMap(CartMap, listCarts)
    collisionFlag, cart1, cart2 = CheckAllCollision()
    if collisionFlag:
        print "Found a collision!"
        PrintCollision(cart1, cart2)
        PrintMap(CartMap,listCarts)
        break





"""
while not collisionFlag:
    tick += 1
    print tick
    #for cart in listCarts:
        #cart.MoveCart()
    # Find cart to move
    tickDone = False
    while not tickDone:
        next = FindNextCartToMove(listCarts, tick)
        if next:
            listCarts[next].MoveCart()
        else:
            tickDone = True


    #print "Tick = ", tick
    PrintMap(CartMap,listCarts)


    for i, cart1 in enumerate(listCarts):
        for j, cart2 in enumerate(listCarts):
            if i == j:
                continue
            else:
                collisionFlag = CheckCollision(cart1, cart2)

for idx, cart in enumerate(listCarts):
    print "Cart", idx
    print cart.curX, cart.curY
"""
