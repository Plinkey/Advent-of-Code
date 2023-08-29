

raw_data = [3,8,1001,8,10,8,105,1,0,0,21,34,59,76,101,114,195,276,357,438,99999,3,9,1001,9,4,9,1002,9,4,9,4,9,99,3,9,102,4,9,9,101,2,9,9,102,4,9,9,1001,9,3,9,102,2,9,9,4,9,99,3,9,101,4,9,9,102,5,9,9,101,5,9,9,4,9,99,3,9,102,2,9,9,1001,9,4,9,102,4,9,9,1001,9,4,9,1002,9,3,9,4,9,99,3,9,101,2,9,9,1002,9,3,9,4,9,99,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,99,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,99]
program = raw_data.copy()




phase = [0,1,2,3,4]

import itertools
perm = itertools.permutations(phase)

max_signal = 0

#Test1 = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
#program = Test1.copy()

#max_value = 0
#
#output = 0
#
#for p in perm:
#    output = 0
#    for i in p:
#        output = execute([i,output])
#    if output > max_value:
#        max_value = output




#######
# Part 2
#######
phase = [5,6,7,8,9]
perm = itertools.permutations(phase)

""" Apparantly, the inputs will go in this order:
phase[A], 0
phase[B], output
phase[C], output
phase[D], output
phase[E], output
output
output
output
output....
"""

max_value = 0
for p in perm:
    output = executePT2(p)
    if output > max_value:
        max_value = output



test = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
executePT2((9,8,7,6,5))
#######
# 
# OLD CODE BELOW
#
#######




def opAdd(inp):
    # new version
    # Adds B+C stores at program[idx]
    B = inp[0]
    C = inp[1]
    idx = inp[2]
    jumpsToNext = 4 # Uses four positions in program
    program[idx] = B + C
    return jumpsToNext

def opMult(inp):
    # new version
    # Multiplies B*C stores at program[idx]
    B = inp[0]
    C = inp[1]
    idx = inp[2]
    jumpsToNext = 4 # Uses four positions in program
    program[idx] = B * C
    return jumpsToNext

def opSave(value, idx):
    # Use when opcode = 3.  Assume idx is positon of A
    # (A,B) save input value to progam position 50. A(opcode)= 3
    # Example: (3,50) would take an input and store at position 50
    jumpsToNext = 2 # Uses two positions in program
    position = program[idx+1]
    program[position] = value
    return jumpsToNext

def opRecall(value):
    # Use when opcode = 4. Assume idx is position of A
    # (A,B) returns value at program[B]. A(opcode) = 4
    jumpsToNext = 2 # Uses two posotions in program
#    print("The Value is: " + str(value))
    out_value = value
    return out_value, jumpsToNext

def opJumpIfTrue(inp):
    # opcode = 5
    # A = first parameter
    # B = second parameter
    # C = current index
    A = inp[0]
    B = inp[1]
    C = inp[2]
    if A != 0:
        return B # return value of 2nd parameter 
    else:
        return C+3 #no jump, return index of next instruction
    
def opJumpIfFalse(inp):
    # Opcode = 6
    # A = first parameter
    # B = second parameter
    # C = current index
    A = inp[0]
    B = inp[1]
    C = inp[2]
    if A == 0:
        return B # return value of 2nd parameter 
    else:
        return C+3 #no jump, return index of next instruction
    
def opLessThan(inp):
    # Opcode = 7
    # A = first parameter
    # B = second parameter
    # C = third Parameter -- bolean
    A = inp[0]
    B = inp[1]
    C = inp[2]
    if A < B:
        program[C] = 1
    else:
        program[C] = 0
    return 4

def opEqual(inp):
    # Opcode = 8
    # A = first parameter
    # B = second parameter
    # C = third Parameter -- bolean
    A = inp[0]
    B = inp[1]
    C = inp[2]
    if A == B:
        program[C] = 1
    else:
        program[C] = 0
    return 4
    
    

# Parameter mode
# Parameter mode 0 is position mode--parameter value is equal to position-index
# parameter mode 1 is immediate mode -- value is VALUE (no longer index)

def parseOpcode(idx):
    fullCode = program[idx] # up to 5 digit parameter ABCDE
    return [int(x) for x in str("{:05d}".format(fullCode))]
    

def mode(idx):
    digits = parseOpcode(idx)
    # digits = [A,B,C,D,E]
    # A = mode of 3rd parameter
    # B = mode of 2nd parameter
    # C = mode of 1st parameter
    # DE = opcode
    opcode = int(str(digits[-2])+str(digits[-1]))
    modeB = digits[2]
    modeC = digits[1]
    modeD = digits[0]
    B = program[idx+1]
    C = program[idx+2]
    D = program[idx+3]
    if opcode in (1,2): # if opcode is add or mult, then return 4
        # Return inputs for opcode function
        # example: opAdd(2,3,30)
        if modeB == 0: #position mode
            valB = program[B]
        else: # immediate mode
            valB = B
        if modeC == 0: #position mode
            valC = program[C]
        else: #immedaite mode
            valC = C
        valD = D # Parameters that an instruction writes to will never be in immediate mode.
        return valB, valC, valD     
    if opcode in (3,4):
        if modeB == 0: #position mode
            valB = program[B]
        else:
            valB = B
        return valB 
    if opcode in (5,6):
        if modeB == 0:
            valB = program[B]
        else:
            valB = B
        if modeC == 0:
            valC = program[C]
        else:
            valC = C
        return valB, valC, idx
    if opcode in (7,8):
        if modeB == 0:
            valB = program[B]
        else:
            valB = B
        if modeC == 0:
            valC = program[C]
        else:
            valC = C
        valD = D # Parameters that an instruction writes to will never be in immediate mode.
        return valB, valC, valD
    else:
        print("Not a valid Full-length opCode!")



#program = test_program.copy()
input_value = 5
def execute(input_values):
    idx = 0
    counter = 0
    while True:
        digits = parseOpcode(idx)
        opcode = int(str(digits[-2])+str(digits[-1]))
        if opcode == 99:
            break
        elif opcode == 1:
            idx += opAdd(mode(idx))
        elif opcode == 2:
            idx += opMult(mode(idx))
        elif opcode == 3:
#            input_value = input('Please Enter Value: ')
#            input_value = int(input_value)
            v = input_values[counter]
            idx += opSave(v,idx)
            counter += 1
        elif opcode == 4:
            answer, jump = opRecall(mode(idx))
            idx += jump
        elif opcode == 5:
            idx = opJumpIfTrue(mode(idx))
#            print('jump to index = '+str(idx))
        elif opcode == 6:
            idx = opJumpIfFalse(mode(idx))
#            print('jump to index = '+str(idx))
        elif opcode == 7:
            idx += opLessThan(mode(idx))
        elif opcode == 8:
            idx += opEqual(mode(idx))
        else:
            print("you broke something, dumbass")
            print("opcode= " + str(opcode))
            print("index = " + str(idx))
            break
        print("going to index = "+str(idx))
    return answer

def executePT2(AmpInputs):
    idx = 0
    counter = 0
    ampCounter = 0
    while True:
        digits = parseOpcode(idx)
        opcode = int(str(digits[-2])+str(digits[-1]))
        if opcode == 99:
            break
        elif opcode == 1:
            idx += opAdd(mode(idx))
        elif opcode == 2:
            idx += opMult(mode(idx))
        elif opcode == 3:
#            input_value = input('Please Enter Value: ')
#            input_value = int(input_value)
            if counter%2 == 0 and counter <= len(AmpInputs):
                #Then this is the first time amp input
                v = AmpInputs[ampCounter]
                ampCounter += 1
            elif counter == 1:
                #Then this is the input to A the first time around.
                v = 0
            else:
                v = answer
            idx += opSave(v,idx)
            counter += 1
        elif opcode == 4:
            answer, jump = opRecall(mode(idx))
            idx += jump
        elif opcode == 5:
            idx = opJumpIfTrue(mode(idx))
#            print('jump to index = '+str(idx))
        elif opcode == 6:
            idx = opJumpIfFalse(mode(idx))
#            print('jump to index = '+str(idx))
        elif opcode == 7:
            idx += opLessThan(mode(idx))
        elif opcode == 8:
            idx += opEqual(mode(idx))
        else:
            print("you broke something, dumbass")
            print("opcode= " + str(opcode))
            print("index = " + str(idx))
            break
#        print("going to index = "+str(idx))
    return answer







if __name__ == "main":
    # Stuff goes here to execute directly.
    a = 1
