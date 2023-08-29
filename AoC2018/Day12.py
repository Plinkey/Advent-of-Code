""" Advent of Code 2018 Day 12"""

#with open('Inputs\Day12TEST.input','r') as f:
    #rawData = f.read().splitlines()


with open('Inputs\Day12.input','r') as f:
    rawData = f.read().splitlines()

## Initial State
initialState = rawData[0].split(':')[1].lstrip(' ')


def ParseRules(line):
    inpt = line.split(' => ')[0]
    result = line.split(' => ')[1]
    return [inpt, result]

def Rules(strSplit):
    #The plant in question is always idx = 2 (3rd plant from left)
    rules = []
    for line in rawData[2:]:
        rules.append(ParseRules(line))
    for rule in rules:
        if strSplit == rule[0]:
            return rule[1]
    return '.'



# Seeding generation 0

MyPlants = []
stopGen = 20
MyPlants.append('................................................' + initialState + '....................................................................................')

def NextGen(curGen):
    newStr = ''
    for idx in range(len(curGen)):
        if idx - 2 > 0 and idx+3 < len(curGen):
            string = curGen[idx-2:idx+3]
            newChar = Rules(string)
            newStr = newStr + newChar
        else:
            newStr = newStr + '.'
    return newStr

for i in range(stopGen):
    MyPlants.append(NextGen(MyPlants[i]))

total = 0

potNum = range(-48,183)
sum = 0
plant = MyPlants[20] 

for idx in range(len(plant)):
    if plant[idx] == '#':
        sum = sum + potNum[idx]

print sum





############
# Part 2
############
MyPlants = []
stopGen =50000000000 

padding = '.'*5000
MyPlants.append(padding + initialState + padding)
MyPlants.append(padding + initialState + padding)

potNum = range(-5000,5000+len(initialState))

# Just going to watch this and look for a pattern
nGen = 0
while True:
    nGen += 1
    MyPlants[0] = MyPlants[1]
    MyPlants[1] = NextGen(MyPlants[0])
    prevSum = sum
    sum = 0
    for jdx in range(len(MyPlants[1])):
        if MyPlants[1][jdx] == '#':
            sum += potNum[jdx]
    print nGen, sum, sum-prevSum
#print nGen, sum


# A ha! every generation after 300 adds 138
# value at gen 100 = 56823 
print ((50000000000-300)*186)+56823.

"""
nGen = 0
while nGen < stopGen:
    nGen += 1
    MyPlants[0] = MyPlants[1]
    MyPlants[1] = NextGen(MyPlants[0])
    sum = 0
    for jdx in range(len(MyPlants[1])):
        if MyPlants[1][jdx] == '#':
            sum += potNum[jdx]
    #print nGen, sum
print nGen, sum
"""


"""while nGen < stopGen:
    # Swap Generations
    MyPlants[0] = MyPlants[1]
    MyPlants[1] = NextGen(MyPlants[0])
    nGen += 1
plant = MyPlants[1]
for idx in range(len(plant)):
    if plant[idx] == '#':
        sum = sum + potNum[idx]
"""
"""
for i in range(stopGen):
    MyPlants.append(NextGen(MyPlants[i]))
total = 0
plant = MyPlants(stopGen)
for idx in range(len(plant)):
    if plant[idx] == '#':
        sum = sum + potNum[idx]

print sum

"""



















""""
oo
for GenIdx in range(stopGen):
    curGen = MyPlants[GenIdx]
    newStr = ''
    for plantIdx in range(len(curGen)):
        if plantIdx-2 > 0 and plantIdx+3 < len(curGen):
            string = curGen[plantIdx-2:plantIdx+3]
            newChar = Rules(string)
            newStr = newStr + newChar
        else:
            newStr = newStr + '.'
    print newStr
    MyPlants.append(newStr)
    """



"""
for GenIdx in range(stopGen-1):
    for plantIdx in range(2,len(MyPlants[GenIdx])-3):
        string = MyPlants[GenIdx][plantIdx-2:plantIdx+3]
        print string
        for rule in rules:
            newChar = RunRule(string, rule[0], rule[1])
            if newChar:
                newStr = MyPlants[GenIdx+1][:plantIdx] + newChar + MyPlants[GenIdx+1][plantIdx+1:]
                MyPlants[GenIdx+1] = newStr

        #for rule in rules:
        #    newChar = RunRule(string, rule[0], rule[1])
        #    print newChar
        #    newStr = MyPlants[GenIdx+1][:plantIdx] + newChar + MyPlants[GenIdx+1][plantIdx+1:]
"""
#print MyPlants[20][10-3:38]
#print RunRule('.....', rules[0][0],rules[0][1])


#for plant in MyPlants:
    #print plant[10-3:38]
