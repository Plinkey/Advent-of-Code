""" Advent Of Code Day 15"""
"""  This one is going to be difficult."""

import numpy as np

with open('Inputs\Day15.input', 'r') as f:
    rawData = f.read().splitlines()

curMap = np.zeros((len(rawData),len(rawData[0])),'str')

for idx, line in enumerate(rawData):
    for jdx, char in enumerate(line):
        curMap[(idx, jdx)] = char


def DisplayMap():
    for line in curMap:
        print ''.join(line)
        # TODO: for each line, print unit and HP (like in examples from site)

DisplayMap()



# Pseudo code below to help plan each ROUND:

# Round BEGINS:

# create list of all units in order
roundOrder = FindUnitOrder()

# all units execute round, in order
for unit in roundOrder:
    curUnit = Units[roundOrder]  
    # Check if curUnit was defeated this round (i.e. status == 'Dead')
    if curUnit.status == 'Dead':
        #unit is dead, skip this guy
        continue
    else:
        curUnit.Move():
            """ 1) identify all possible targets
                2) identify open squares around all targets
                3) identify squares from #2 that can be reached 
                4) identify squares from #3 that are the closest
                    4a) If no path can be found, end and proceed to attack
                5) Move to square based on READING ORDER
            """
        curUnit.Attack():
            """ 1) Determine all enemy units in range
                    1a) If no enemies, end turn
                2) Target enemy with fewest HP remaining
                3) Reduce target enemy HP by curUnit's AP
                4) Check target enemy is still alive
                    4a) if HP <= 0, update target status == 'Dead'
                    4b) update map with target's location as open == '.'
            """
            
