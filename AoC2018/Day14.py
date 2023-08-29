
""" Advent Of Code """
import numpy as np



##############
#   Helper Functions
##############



def Rotate(array, curIdx):
    score = array[curIdx]
    length = len(array)
    return ((curIdx+1)+score)%length

def NextGenRecipe(array, idx1, idx2):
    strSum = str(array[idx1] + array[idx2])
    for i in strSum:
        array.append(int(i))
    return array, len(strSum)

##############
# Part A
##############

recipeArray = [3,7]
# Test Case below. should  = 5158916779
#goalRecipe = 9 # This is the ELF's GOAL
# Test Case below. should = 0124515891
#goalRecipe= 5 # This is the ELF's GOAL
# Test case belwo should = 9251071085
#goalRecipe = 18
# Test case below shoul = 5941429882
#goalRecipe = 2018


# Puzzle Input below:
goalRecipe = 702831


elf1 = 0
elf2 = 1

nRecipes = 2

""" uncomment for part 1
while nRecipes <= goalRecipe + 10:
    recipeArray, newRecipes = NextGenRecipe(recipeArray, elf1, elf2)
    nRecipes += newRecipes
    elf1 = Rotate(recipeArray, elf1)
    elf2 = Rotate(recipeArray, elf2)
    print "Total Num of Recipes so far = ", nRecipes

#print recipeArray
print "len recipeArray = ", len(recipeArray)
answer = ''
for i in recipeArray[goalRecipe:goalRecipe+10]:
    answer += str(i)

print recipeArray[-11:]
print "The Answer IS =", answer
"""


##############
# Part B
##############

print " " 
print "*************part two**********************"
print " " 

def FindSequence(array, sequence):
    # Split sequence into digits, assume sequence is str 
    seq = []
    #for i in str(sequence):
        #seq.append(int(i))
    for i in sequence:
        seq.append(int(i))
    i, n, m = -1, len(array), len(seq)
    try:
        while True:
            i = array.index(seq[0], i+1, n-m+1)
            if seq == array[i:i+m]:
                return i
    except ValueError:
        return -1

def NextGenRecipe2(array, idx1, idx2):
    strSum = str(array[idx1] + array[idx2])
    for i in strSum:
        array[np.where(array==-1)[0][0]] = int(i)
        #array.append(int(i))
    return array, len(strSum)



#recipeArray = [3,7]
recipeArray = np.zeros(1000000)
recipeArray.fill(-1) # using -1 as flag
recipeArray[0] = 3
recipeArray[1] = 7

elf1 = 0
elf2 = 1
# Test case should = 9
#sequence = '51589'
# Test case should = 5
#sequence = '01245'
# Test case should = 18
#sequence = '92510'
# Test case should = 2018
#sequence = '59414'

sequence = '702830'

foundFlag = -1



 """
 #  uncomment for part 1
while nRecipes <= goalRecipe + 10:
    recipeArray, newRecipes = NextGenRecipe2(recipeArray, elf1, elf2)
    nRecipes += newRecipes
    elf1 = Rotate(recipeArray, elf1)
    elf2 = Rotate(recipeArray, elf2)
    if nRecipes%1000 == 0:
        print "Total Num of Recipes so far = ", nRecipes

#print recipeArray
print "len recipeArray = ", len(recipeArray)
answer = ''
for i in recipeArray[goalRecipe:goalRecipe+10]:
    answer += str(i)

print recipeArray[-11:]
print "The Answer IS =", answer
"""
while foundFlag == -1:
    recipeArray, newRecipes = NextGenRecipe2(recipeArray, elf1, elf2)
    nRecipes += newRecipes
    foundFlag = FindSequence(recipeArray, sequence)
    elf1 = Rotate(recipeArray, elf1)
    elf2 = Rotate(recipeArray, elf2)
    if nRecipes%1000 == 0:
        print "Total Num of Recipes so far = ", nRecipes
#print recipeArray
print foundFlag
"""
