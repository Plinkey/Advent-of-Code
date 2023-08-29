""" Advent of Code 2018 Day 7"""

with open('Inputs\Day7.input','r') as f:
    rawData = f.read().splitlines()


from collections import defaultdict
rule = defaultdict(list)
num = defaultdict(int)
for line in rawData:
    splits = line.split(' ')
    rule[splits[1]].append(splits[7])
    num[splits[7]] += 1

# sort the lists inside key lsit. (the AFTER part)
# Hopefully this'll take care of the alphabetical part
for idx in rule:
    rule[idx] = sorted(rule[idx])


Queue = []
WorkDone = []


def DoTask(task):
    global Queue
    Queue.pop(Queue.index(task))
    WorkDone.append(task)
    for letter in rule:
        i = rule[letter]
        i = [a for a in i if a != task] #remove task from list
    array = rule[task]
    for i in array:
        num[i] -= 1
    num[task] -= 1


def FindNext():
    for idx in rule:
        if num[idx] == 0: # it's the only letter with no precidents
            #print Queue, idx, idx in Queue
            if idx not in Queue:
                if idx not in WorkDone:
                    Queue.append(idx)

while max(num.values()) >= 0:
#i = 0
#while i < 13:
    #i += 1
    print WorkDone
    print Queue
    FindNext()
    DoTask(min(Queue))

print len(WorkDone)
print Queue
print WorkDone

###########
# PART II 
###########
