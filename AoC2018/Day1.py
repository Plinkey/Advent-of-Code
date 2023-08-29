""" Advent of Code Day 1"""
import numpy as np

data = np.loadtxt("Inputs\Day1.input", delimiter=',')


#########
## PART 1
#########

#Initialize
freq = 0.

#Loop
for value in data:
    freq = freq + value

#Print Answer
print freq



#########
## PART 2
#########

#Reset Everything and Initialize
freq = 0.
listFreq = []
listFreq.append(0.)
found = False

#Keep looping through input until you find a matching freq
while not found:
    for value in data:
        freq = freq + value
        if freq in listFreq:
            found = True
            print freq
            break
        else:
            listFreq.append(freq)

