debug = False


# %% Load Inputs
if debug:
    with open('Day08.example', 'r') as f:
        data = f.read().splitlines()
else:    
    with open('Day08.input', 'r') as f:
        data = f.read().splitlines()
        


# %%
# Do Stuff with input string.
def process(inline):
    instr = data[inline]
    command, num = instr.split(' ')
    return command, int(num)

# %%
# ACC command
def acc(lineNo):
    command, num = process(lineNo)
    seenLines.append(lineNo)
    global accumulator
    accumulator += num
    if debug:
        print('On Line: {}, the accumulator is {}'.format(lineNo, accumulator))
    return lineNo+1

# %%
# NOP command
def nop(lineNo):
    command, num = process(lineNo)
    seenLines.append(lineNo)
    return lineNo+1

# %%
# JMP command
def jmp(lineNo):
    command, num = process(lineNo)
    seenLines.append(lineNo)
    return lineNo + num

# %%
def runLine(lineNo, data=data):
    if 'nop' in data[lineNo]:
        nextLine = nop(lineNo)
    elif 'jmp' in data[lineNo]:
        nextLine = jmp(lineNo)
    elif 'acc' in data[lineNo]:
        nextLine = acc(lineNo)
    return nextLine


    
def runIt(data):
    global seenLines
    seenLines = []
    global accumulator
    accumulator = 0
    curLine = 0
    while True:
        if curLine in seenLines:
            print('The answer to part one is: {}'.format(accumulator))
            break
        curLine = runLine(curLine)

runIt(data)
            
    
# %%
# Part Two


#%%
# def resetData():
#     if debug:
#         with open('Day08.example', 'r') as f:
#             data = f.read().splitlines()
#     else:    
#         with open('Day08.input', 'r') as f:
#             data = f.read().splitlines()
#     return data

def changeThisLine(lineNo):
    cmd, num = process(lineNo)
    if cmd == 'nop':
        new = 'jmp'
    else:
        new = 'nop'
    return '{} {}'.format(new, num)

# %%
# def part2Trial(changeLine):    
#     flag = True
#     while True:
#         print(seenLines)
#         if curLine in seenLines:
#             print('Infinite Loop. changeLine: {}'.format(changeLine))
#             return flag
#         elif curLine == len(data):
#             print('The answer to part two is: {}'.format(accumulator))
#             flag = False
#             return flag
#         print('the current line(error): {}'.format(curLine))
#         curLine = runLine(curLine)

def part2Trial(indata):
    global seenLines
    seenLines = []
    global accumulator
    accumulator = 0
    curLine = 0
    flag = False
    # print('#### STARTING NEW TRIAL###')
    while True:
        print(seenLines)
        if curLine in seenLines:
            # flag = True
            # print('### Ending trial due to curline in seen lines')
            print('curline: {}, seenlines: {}'.format(curLine, seenLines))
            return flag
        elif curLine == len(indata):
            print('The answer to part two is: {}'.format(accumulator))
            flag = True
            return flag
        print(indata[curLine])
        curLine = runLine(curLine, data = indata)
        # print('new curLine: {}'.format(curLine))
        

def part2RunIt():
    changeLine = 0
    while True:
        d = data.copy()
        if 'jmp' in d[changeLine] or 'nop' in d[changeLine]:
            # print('changing line {}'.format(changeLine))
            d[changeLine] = changeThisLine(changeLine)
            if d[changeLine] == 'jmp 0':
                changeLine += 1
                continue
            # print(d)
            flag = part2Trial(d)
            if flag:
                break
            changeLine += 1
        else:
            changeLine += 1
            
            
part2RunIt()

"""
changeLine = 0
while True:
    print('The changeLine is now: {}'.format(changeLine))
    if 'jmp' in data[changeLine] or 'nop' in data[changeLine]:
        flag = part2Trial(changeLine)
        if flag:
            changeLine += 1
            data = resetData()
        else:
            break
    else:
        changeLine += 1
"""
            
            
            
            
            
            
            
            
            
            
            
            
            
        
        
        