

"""
Notes from reading text
Opcode 99 -- halt
Opcode 1 -- add two and store in third
    (A,B,C,D,E)  A - opcode
                 B - positions where to read
                 C
                 D - position to store
                
Opcode 2 - multiply

Move to next by stepping forward 4 positions
"""

# Bad form--copy/paste input
raw_input = [3,225,1,225,6,6,1100,1,238,225,104,0,1102,88,66,225,101,8,125,224,101,-88,224,224,4,224,1002,223,8,223,101,2,224,224,1,224,223,223,1101,87,23,225,1102,17,10,224,101,-170,224,224,4,224,102,8,223,223,101,3,224,224,1,223,224,223,1101,9,65,225,1101,57,74,225,1101,66,73,225,1101,22,37,224,101,-59,224,224,4,224,102,8,223,223,1001,224,1,224,1,223,224,223,1102,79,64,225,1001,130,82,224,101,-113,224,224,4,224,102,8,223,223,1001,224,7,224,1,223,224,223,1102,80,17,225,1101,32,31,225,1,65,40,224,1001,224,-32,224,4,224,102,8,223,223,1001,224,4,224,1,224,223,223,2,99,69,224,1001,224,-4503,224,4,224,102,8,223,223,101,6,224,224,1,223,224,223,1002,14,92,224,1001,224,-6072,224,4,224,102,8,223,223,101,5,224,224,1,223,224,223,102,33,74,224,1001,224,-2409,224,4,224,1002,223,8,223,101,7,224,224,1,223,224,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,107,677,677,224,1002,223,2,223,1006,224,329,101,1,223,223,108,677,677,224,1002,223,2,223,1005,224,344,101,1,223,223,1007,677,677,224,1002,223,2,223,1006,224,359,101,1,223,223,1107,226,677,224,1002,223,2,223,1006,224,374,1001,223,1,223,8,677,226,224,1002,223,2,223,1006,224,389,101,1,223,223,1108,677,677,224,1002,223,2,223,1005,224,404,1001,223,1,223,7,226,226,224,1002,223,2,223,1006,224,419,101,1,223,223,1107,677,677,224,1002,223,2,223,1005,224,434,101,1,223,223,107,226,226,224,102,2,223,223,1005,224,449,101,1,223,223,107,677,226,224,1002,223,2,223,1006,224,464,1001,223,1,223,8,226,677,224,102,2,223,223,1006,224,479,1001,223,1,223,108,677,226,224,102,2,223,223,1005,224,494,1001,223,1,223,1108,677,226,224,1002,223,2,223,1005,224,509,1001,223,1,223,1107,677,226,224,1002,223,2,223,1005,224,524,101,1,223,223,1008,226,226,224,1002,223,2,223,1006,224,539,101,1,223,223,1008,226,677,224,1002,223,2,223,1005,224,554,1001,223,1,223,7,226,677,224,1002,223,2,223,1005,224,569,101,1,223,223,1007,677,226,224,1002,223,2,223,1006,224,584,1001,223,1,223,7,677,226,224,102,2,223,223,1006,224,599,101,1,223,223,1007,226,226,224,102,2,223,223,1006,224,614,101,1,223,223,1008,677,677,224,1002,223,2,223,1006,224,629,101,1,223,223,108,226,226,224,102,2,223,223,1006,224,644,101,1,223,223,1108,226,677,224,1002,223,2,223,1005,224,659,101,1,223,223,8,226,226,224,1002,223,2,223,1005,224,674,101,1,223,223,4,223,99,226]
program = raw_input.copy()

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
    print(str(value))
    return jumpsToNext

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

test_program = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]

#program = test_program.copy()
input_value = 5
def execute():
    idx = 0
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
            idx += opSave(input_value,idx)
        elif opcode == 4:
            idx += opRecall(mode(idx))
        elif opcode == 5:
            idx = opJumpIfTrue(mode(idx))
            print('jump to index = '+str(idx))
        elif opcode == 6:
            idx = opJumpIfFalse(mode(idx))
            print('jump to index = '+str(idx))

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






