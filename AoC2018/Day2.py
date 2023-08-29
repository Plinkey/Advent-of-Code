""" Advent of Code Day 2 """


#######
# Import Data
#######

with open('Inputs\Day2.input','r') as f:
    data = f.read().splitlines()

# below is example for debug
#data = ['abcde','fghij','klmno','pqrst','fguij','axcye','wvxyz']


#######
# Part 1
#######

nTwo    = 0  # Number of IDs with two letters
nThree  = 0  # Number of IDs with three letters

for ID in data:
    charFreq = {}
    
    # Loop through ID and find character frequencies
    for char in ID:
        if char in charFreq.keys():
            charFreq[char] = charFreq[char] + 1
        else:
            charFreq[char] = 1
    
    # Find if any character is appears exactly twice
    for char, freq in charFreq.items():
        if freq == 2:
            nTwo += 1
            break

    # Find if any character appears exactly three times
    for char, freq in charFreq.items():
        if freq == 3:
            nThree += 1
            break
    

# Calc checksum
checksum = nTwo * nThree

print checksum


#######
# Part 2
#######

badCharPos = 0

for ID in data:
    for compare in data:
        # first, skip the case where ID == compare:
        if ID == compare:
            continue
        else:
            # loop through and check if positions are the same
            wrongChar = []
            for idx, char in enumerate(ID):
                if ID[idx] != compare[idx]:
                    wrongChar.append(idx)
            if len(wrongChar) == 1:
                candidate_ID = ID
                badCharPos = wrongChar[0]

# Answer, the letters in common IN ORDER:
str1 = candidate_ID[:badCharPos]
str2 = candidate_ID[badCharPos+1:]
print str1+str2
