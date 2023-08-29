""" Advent of Code Day 16 """
import numpy as np

#################
# Functions
#################


# Addition
def ADDR(a,b,c):
    out = stack.copy()
    out[c] = stack[a] + stack[b]
    return out


def ADDI(a,b,c):
    out = stack.copy()
    out[c] = stack[a] + b
    return out

# Multiplication
def MULR(a,b,c):
    out = stack.copy()
    out[c] = stack[a] * stack[b]
    return out

def MULI (a,b,c):
    out = stack.copy()
    out[c] = stack[a] * b
    return out

def BORR(a,b,c):
    out = stack.copy()
    out[c] = stack[a] | stack[b]
    return out

def BORI(a,b,c):
    out = stack.copy()
    out[c] = stack[a] | b
    return out

# Assignment
def SETR(a,b,c):
    out = stack.copy()
    out[c] = stack[a]
    return out
    # ignore b

def SETI(a,b,c):
    out = stack.copy()
    out[c] = a
    return out
    # ignore b

# Greater thant tests
def GTIR(a,b,c):
    out = stack.copy()
    if a > stack[b]:
        out[c] = 1
    else:
        out[c] = 0
    return out
    

def GTRI(a,b,c):
    out = stack.copy()
    if stack[a] > b:
        out[c] = 1
    else:
        out[c] = 0
    return out

def GTRR(a,b,c):
    out = stack.copy()
    if stack[a] > stack[b]:
        out[c] = 1
    else:
        out[c] = 0
    return out

# Equality
def EQIR(a,b,c):
    out = stack.copy()
    if a == stack[b]:
        out[c] = 1
    else:
        out[c] = 0
    return out

def EQRI(a,b,c):
    out = stack.copy()
    if stack[a] == b:
        out[c] = 1
    else:
        out[c] = 0
    return out

def EQRR(a,b,c):
    out = stack.copy()
    if stack[a] == stack[b]:
        out[c] = 1
    else:
        out[c] = 0
    return out

def BANR(a,b,c):
    out = stack.copy()
    out[c] = stack[a] & stack[b]
    return out

def BANI(a,b,c):
    out = stack.copy()
    out[c] = stack[a] & b
    return out

    


###################
# Parse part 1 lines
###################

def ParsePartOne(lines_in):
    # Before
    before = lines_in[0].split(': ')[1]
    before = before.lstrip('[').rstrip(']').split(', ')
    for i, val in enumerate(before):
        before[i] = int(val)

    # Operation
    op = lines_in[1].split(' ')
    for i, val in enumerate(op):
        op[i] = int(val)

    # After
    after = lines_in[2].split(':  ')[1]
    after = after.lstrip('[').rstrip(']').split(', ')
    for i, val in enumerate(after):
        after[i] = int(val)

    return np.array(before), np.array(op), np.array(after)



###################
# Check what operations are True
###################

def Compare(a,b):
    for idx, value in enumerate(a):
        if b[idx] != value:
            return False
            break
    return True

def CheckWhatsTrue(lines_in):
    global stack
    truth = np.zeros(16, 'int')
    # list of all 
    """ indices:
        0 = ADDR
        1 = ADDI
        2 = MULR
        3 = MULI
        4 = BORR
        5 = BORI
        6 = SETR
        7 = SETI
        8 = GTIR
        9 = GTRI
        10 = GTRR
        11 = EQIR
        12 = EQRI
        13 = EQRR
        14 = BANR
        15 = BANI
    """
    stack, operation, stackPost = ParsePartOne(lines_in)
    nOP = operation[0]
    #if stackPost == ADDR(operation[1], operation[2], operation[3]):
    if Compare(stackPost,ADDR(operation[1], operation[2], operation[3])):
        truth[0] = 1
    if Compare(stackPost, ADDI(operation[1], operation[2], operation[3])):
        truth[1] = 1
    if Compare(stackPost, MULR(operation[1], operation[2], operation[3])):
        truth[2] = 1
    if Compare(stackPost, MULI(operation[1], operation[2], operation[3])):
        truth[3] = 1
    if Compare(stackPost, BORR(operation[1], operation[2], operation[3])):
        truth[4] = 1
    if Compare(stackPost, BORI(operation[1], operation[2], operation[3])):
        truth[5] = 1
    if Compare(stackPost, SETR(operation[1], operation[2], operation[3])):
        truth[6] = 1
    if Compare(stackPost, SETI(operation[1], operation[2], operation[3])):
        truth[7] = 1
    if Compare(stackPost, GTIR(operation[1], operation[2], operation[3])):
        truth[8] = 1
    if Compare(stackPost, GTRI(operation[1], operation[2], operation[3])):
        truth[9] = 1
    if Compare(stackPost, GTRR(operation[1], operation[2], operation[3])):
        truth[10] = 1
    if Compare(stackPost, EQIR(operation[1], operation[2], operation[3])):
        truth[11] = 1
    if Compare(stackPost, EQRI(operation[1], operation[2], operation[3])):
        truth[12] = 1
    if Compare(stackPost, EQRR(operation[1], operation[2], operation[3])):
        truth[13] = 1
    if Compare(stackPost, BANR(operation[1], operation[2], operation[3])):
        truth[14] = 1
    if Compare(stackPost, BANI(operation[1], operation[2], operation[3])):
        truth[15] = 1


    print truth
    return truth

def CountTruth(truth):
    return len(np.where(truth==1)[0])


with open('Inputs\Day16a.input', 'r') as f:
    rawData = f.read().splitlines()

"""
line1 = 'Before: [3, 2, 1, 1]'
line2 = '9 2 1 2'
line3 = 'After:  [3, 2, 2, 1]'
lines = [line1, line2, line3]
truth = CheckWhatsTrue(lines)
nTruth = CountTruth(truth)
print nTruth
"""

"""
line1 = rawData[4]
line2 = rawData[4+1]
line3 = rawData[4+2]
lines = [line1, line2, line3]
print lines

#ParsePartOne(lines)
truth = CheckWhatsTrue(lines)
print truth
"""

counter = 0
count = 0
while counter <= len(rawData):
    line1 = rawData[counter]
    #print line1
    line2 = rawData[counter+1]
    #print line2
    line3 = rawData[counter+2]
    #print line3
    lines = [line1, line2, line3]
    #print lines
    truth = CheckWhatsTrue(lines)
    nTruth =  CountTruth(truth)
    if  nTruth >= 3:
        count += 1
    counter += 4

print "THE ANWSER IS: ", count
