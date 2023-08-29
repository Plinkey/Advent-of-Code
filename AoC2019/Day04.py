def checkValid(password):
    digits = [int(x) for x in str(password)]
    lengthFlag = checkLength(digits)
    #print ("Length Flag= " + str(lengthFlag))
    if not lengthFlag:
        return False
    adjacentFlag = checkAdjacent(digits)
    #print ("Adjacent Flag= " + str(adjacentFlag))
    if not adjacentFlag:
        return False
    LR_Flag = checkLeftRight(digits)
    #print ("LR Flag= " + str(LR_Flag))
    if not LR_Flag:
        return False
    part2Flag = checkAdjacentPart2(digits)
    #print ("part2 Flag= " + str(part2Flag))

    if not part2Flag:
        return False
    return True



def checkLength(digits):
    # Is a 6-digit number
    if len(digits) != 6:
        return False
    return True

# The value is within the range given in your puzzle input
# I'll handle this one outside this check so I can assert the examples

def checkAdjacent(digits):
    # Two adjacent digits are the same (like 22 in 122345)
    for idx in range(len(digits)):
        jdx = idx + 1
        if jdx < len(digits):
            if digits[idx] == digits[jdx]:
                return True
    return False



def checkLeftRight(digits):
    # Going from left to right, the digits *NEVER DECREASE*  only increase or same
    # Examples:  111123 or 135679
    for idx in range(len(digits)):
        jdx = idx + 1
        if jdx < len(digits):
            if digits[jdx] < digits[idx]:
                return False
    return True

def checkAdjacentPart2(digits):
    nAdjacentSets = 0 # count of adjacent number sets
    numDict = {}
    for idx in range(len(digits)):
        jdx = idx + 1
        if jdx < len(digits):
            if digits[idx] == digits[jdx]:
                nAdjacentSets += 1
                if digits[idx] in numDict:
                    numDict[digits[idx]] += 1
                else:
                    numDict[digits[idx]] = 1
    # search through numDict and find:
    #print numDict
    if nAdjacentSets > 0:
        if 1 not in numDict.values(): # one means one double (no trip or above)
            return False
    return True


checkValid(111111)
checkValid(223450)
checkValid(123789)


nValid = 0
passMin = 245182 # input from problem
passMax = 790572 # input from problem

for passwd in range(passMin, passMax+1):
    if checkValid(passwd):
        nValid += 1

print ("Part 1 answer = " + str(nValid))


## Part 2
checkValid(112233) #should be true
checkValid(123444) #should be false
checkValid(111122) # should be true

nValid = 0
for passwd in range(passMin, passMax+1):
    if checkValid(passwd):
        nValid += 1

print ("Part 2 answer = " + str(nValid))       
