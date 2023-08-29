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

def opAdd(start, program):
    #(A,B,C,D,E) assume start is position of A
    # Add value at B to value at C and store at position D
    store_idx = program[start+3]
    B_idx     = program[start+1]
    C_idx     = program[start+2]
    program[store_idx] = program[B_idx] + program[C_idx]
    return program

def opMult(start, program):
    #(A,B,C,D,E) assume start is position of A
    # multiply value at B to value at C and store at position D
    store_idx = program[start+3]
    B_idx     = program[start+1]
    C_idx     = program[start+2]
    program[store_idx] = program[B_idx] * program[C_idx]
    return program

test = [1,9,10,3,2,3,11,0,99,30,40,50]
opAdd(0,test)
opMult(4,test)

#don't judge me for copy/paste input
raw_input = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,13,19,1,10,19,23,2,9,23,27,1,6,27,31,1,10,31,35,1,35,10,39,1,9,39,43,1,6,43,47,1,10,47,51,1,6,51,55,2,13,55,59,1,6,59,63,1,10,63,67,2,67,9,71,1,71,5,75,1,13,75,79,2,79,13,83,1,83,9,87,2,10,87,91,2,91,6,95,2,13,95,99,1,10,99,103,2,9,103,107,1,107,5,111,2,9,111,115,1,5,115,119,1,9,119,123,2,123,6,127,1,5,127,131,1,10,131,135,1,135,6,139,1,139,5,143,1,143,9,147,1,5,147,151,1,151,13,155,1,5,155,159,1,2,159,163,1,163,6,0,99,2,0,14,0]
#making a copy so resetting is easier
program = raw_input.copy()

#replace position 1 with value of position 12
program[1] = 12

#replace position 2 with the value 2
program[2] = 2

#Loop everything. Halt when  opcode = 99

idx = 0
while True:
    if program[idx] == 99:
        break
    elif program[idx] == 1:
        opAdd(idx, program)
    elif program[idx] == 2:
        opMult(idx, program)
    else:
        print("you broke something, dumbass")
    idx += 4
    
program[0]


#############################
# Part 2
#############################
#copy of above
def execute():
    idx = 0
    while True:
        if program[idx] == 99:
            break
        elif program[idx] == 1:
            opAdd(idx, program)
        elif program[idx] == 2:
            opMult(idx, program)
        else:
            print("you broke something, dumbass")
        idx += 4
     
program = raw_input.copy()

noun = list(range(0,99))
verb = list(range(0,99))

for n in noun:
    for v in verb:
        program[1] = n
        program[2] = v
        execute()
        output = program[0]
        if output == 19690720:
            print('CORRECT ANSWER')
            print('NOUN: ' + str(n))
            print('VERB: ' + str(v))
            print('Answer: ' + str(100*n+v))
            break
        else:
            program = raw_input.copy()
