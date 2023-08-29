#################
#
#  AOC DAY 16
#
#################



import numpy as np

"""
15243  =>  1,5,2,4,3

New list same length as old list

each element in new list: multiply every value in input by a value in a repeating pattern
Example: 9,8,7,6,5
Pattern: 1,2,3
9*1+8*2+7*3+6*1+5*2
THEN keep only the ones digit ((abs) % 10)

PATTERN:
base: 0,1,0,-1
repeat each value in the pattern a number of times equal to the position in the output list

First:
0,1,0,-1

Second:
0,0,1,1,0,0,-1,-1

Third:
0,0,0,1,1,1,0,0,0,-1,1,-1

**BUT**
Offset the first value by one:
REAL second:
0,1,1,0,0,-1,-1


"""

import copy

###############
#
# Inputs
#
###############

# puzzle input
input_str = "59728839950345262750652573835965979939888018102191625099946787791682326347549309844135638586166731548034760365897189592233753445638181247676324660686068855684292956604998590827637221627543512414238407861211421936232231340691500214827820904991045564597324533808990098343557895760522104140762068572528148690396033860391137697751034053950225418906057288850192115676834742394553585487838826710005579833289943702498162546384263561449255093278108677331969126402467573596116021040898708023407842928838817237736084235431065576909382323833184591099600309974914741618495832080930442596854495321267401706790270027803358798899922938307821234896434934824289476011"


# Example 1
#input_str = "12345678"

# Example 2 -- after 100 phases, should become 24176176
#input_str = "80871224585914546619083218645595"

# Example 3 -- after 100 phases, should become 73745418
# input_str = "19617804207202209144916044189917"

# Example 4 -- after 100 phases, should become 52432133
# input_str = "69317163492948606335995924319873"




###############
#
# Process Input
#
###############

data = np.array([int(i) for i in input_str],dtype='int')


###############
#
# Create Pattern
# and helper functions
#
###############
def pattern(idx, offset = 1):
    base = [0,1,0,-1]
    a = [base[0]]*idx
    b = [base[1]]*idx
    c = [base[2]]*idx
    d = [base[3]]*idx
    output = a+b+c+d
    output = output*len(data)
    return np.array(output[offset:len(data)+1],dtype='int')
    

def rotate_pattern(inlist, num = -1):
    outlist = np.roll(inlist, num)
    return outlist

   



###############
#
# Calculate element
#
###############
def calc_element(data, pat,pnum):
    # pnum = position number in final output
    output = 0
    output = sum(data * pat)
    return abs(output)%10




max_phase = 100
curSignal = np.zeros([2,len(data)],dtype='int')
curSignal[0][:] = data
curSignal[1][:] = data
dataLen = len(data)

fullPattern= np.zeros([len(data),len(data)],dtype='int')
for idx in range(dataLen):
    fullPattern[idx][:] = pattern(idx+1)


for nPhase in range(max_phase):
    curSignal[0] = curSignal[-1]
    nPhase += 1
    print('processing phase: '+str(nPhase))
    for idx in range(dataLen):
        curSignal[1][idx] = calc_element(curSignal[0][:],fullPattern[idx],idx)

    
# answer
print(curSignal[1][0:8])



#############################
#
#  PART B
#
#############################

# Example 5 -- after 100 phases, should become 84462026
#input_str = "03036732577212944063491565474664"

# Example 6 -- after 100 phases, should become 78725270
# input_str = "02935109699940807407585447034323"

# Example 7 -- after 100 phases, should become 53553731
# input_str = "03081770884921959731165446850517"



        
offset = int(input_str[:7], 10)
input_list = list(map(int, input_str)) * 10000
input_length = len(input_list)

for i in range(100):
    partial_sum = sum(input_list[j] for j in range(offset, input_length))
    for j in range(offset, input_length):
        t = partial_sum
        partial_sum -= input_list[j]
        if t >= 0:
            input_list[j] = t % 10
        else:
            input_list[j] = (-t) % 10

            
print(input_list[offset: offset+8])
    
