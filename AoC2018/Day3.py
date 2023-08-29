""" Advent of Code 2018 Day 3"""
import numpy as np

########################
# PART 1
########################

## some object classes to help things
class Claim:
    def __init__(self, ID, l, t, w, h):
        self.ID     = ID
        self.left   = l
        self.top    = t
        self.width  = w
        self.height = h

class Fabric:
    def __init__(self, width, height):
        import numpy as np
        x = np.linspace(0,width-1,width)
        y = np.linspace(0,height-1,height)
        xx,yy = np.meshgrid(x,y)
        self.xx = xx
        self.yy = yy
        self.nClaims = np.zeros((width,height))



## Some helper functions
# Split up Raw Data
def SplitRawData(rawData):
    temp = rawData.split(' ')
    ID = int(temp[0].strip('#'))
    temp2 = temp[2].strip(':').split(',')
    left  = int(temp2[0])
    right = int(temp2[1])
    temp3 = temp[3].split('x')
    width  = int(temp3[0])
    height = int(temp3[1])
    
    return ID, left, right, width, height

# Function to make claim, increase nClaim by 1
def MakeClaim(Fabric, Claim):
    # start at top-left corner
    for height_idx in range(Claim.height):
        for width_idx in range(Claim.width):
            Fabric.nClaims[height_idx+Claim.top][width_idx+Claim.left] += 1



## OK, let's find the answer

#Test below
#santa = Fabric(10,10)
#test = Claim(9999,2,1,3,5)
#MakeClaim(santa,test)
#test2 = Claim(8888,4,2,2,2)
#MakeClaim(santa,test2)
#test3 = Claim(7777,1,3,4,5)
#MakeClaim(santa,test3)
#print santa.nClaims
#print np.amax(santa.nClaims)


with open('Inputs\Day3.input', 'r') as f:
    rawData = f.read().splitlines()

santa = Fabric(1000,1000)
#loop through rawData and make claim on fabric
for data in rawData:
    ID,l,t,w,h = SplitRawData(data)
    tmpClaim = Claim(ID,l,t,w,h)
    MakeClaim(santa,tmpClaim)

# find anser: HOW MANY SQUARE INCHES OF FABIC ARE WITHIN TWO OR MORE CLAIMS?
print len(np.where(santa.nClaims >= 2)[0])



########################
# PART 2
########################
print "starting Part 2"
#print np.where(santa.nClaims >=1)
#print santa.nClaims
#import matplotlib.pyplot as plt
#plt.matshow(santa.nClaims)
#plt.show()

def FindUnique(Fabric, Claim):
    foundFlag = False
    returnID = 0
    temp = np.zeros((Claim.height, Claim.width))
    for height_idx in range(Claim.height):
        for width_idx in range(Claim.width):
            cur_value = Fabric.nClaims[height_idx+Claim.top][width_idx+Claim.left]
            temp[height_idx][width_idx] = cur_value + 1
    
    if np.amax(temp) == 2:
        foundFlag = True
        returnID = Claim.ID
        return foundFlag, returnID
    else:
        return foundFlag, returnID




for data in rawData:
    ID,l,t,w,h = SplitRawData(data)
    tmpClaim = Claim(ID,l,t,w,h)
    foundFlag, uniqueID = FindUnique(santa,tmpClaim)
    if foundFlag:
        break

print uniqueID
