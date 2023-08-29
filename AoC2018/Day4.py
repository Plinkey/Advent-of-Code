""" ADVENT OF CODE 2018 Day 4"""

# Attempt number 4, I think.
# Getting some help from /r/adventofcode

import collections
import dateutil
import dateutil.parser
guards = collections.defaultdict(list)
times = collections.defaultdict(int)

lines = open('Inputs\Day4.input').read()

for line in sorted(lines.splitlines()):
    time, action = line.split('] ')

    time = dateutil.parser.parse(time[1:])

    if action.startswith('Guard'):
        guard = int(action.split()[1][1:])
    elif action == 'falls asleep':
        start = time
    elif action == 'wakes up':
        end = time
        guards[guard].append((start.minute, end.minute))
        times[guard] += (end - start).seconds

(guard, time) = max(times.items(), key=lambda i: i[1])
(minute, count) = max([
    (minute, sum(1 for start, end in guards[guard] if start <= minute < end))
for minute in range(60)], key=lambda i: i[1])

print('part 1:', guard * minute)

(guard, minute, count) = max([
    (guard, minute, sum(1 for start, end in guards[guard] if start <= minute < end))
for minute in range(60) for guard in guards], key=lambda i: i[2])

print('part 2:', guard * minute)

"""
import re
from collections import Counter
with open("Inputs\Day4.input", "r") as f:
    guards = {}
    start, stop, current_guard = 0, 0, 0
    lines = [x.strip() for x in f.readlines()]

    for line in lines:
        values = re.findall("\d+", line)
        if "Guard" in line:
            current_guard = int(values[-1])
        elif "falls asleep" in line:
            start = int(values[-1])
        elif "wakes up" in line:
            stop = int(values[-1])
            for i in range(start, stop):
                guards.setdefault(current_guard, []).append(i)
    # part 1
    id1 = max(guards, key=lambda x: len(guards[x]))
    c = Counter(guards[id1])
    minute = c.most_common()[0][0]
    print(id1 * minute)
    # part2
    id2 = max(guards, key=lambda x: Counter(guards[x]).most_common()[0][1])
    print(id2 * Counter(guards[id2]).most_common()[0][0])
"""

"""from collections import defaultdict

lines = open('Inputs\Day4.input').read().split('\n')
lines.sort()

def parse(line):
    word = line.split()
    date, time = word[0][1:], word[1][:-1]
    return int(time.split(':')[1])

C = defaultdict(int)
CM = defaultdict(int)
guard = None
asleep = None

for line in lines:
    if line:
        time = parse(line)
        if 'begins shift' in line: #then this starts a new (or repeat) guard
            guard = int(line.split()[3][1:])
            asleep = None
        elif 'falls asleep' in line: #he just fell asleep
            asleep = time
        elif 'wakes up' in line: # he just woke up
            for t in range(asleep,time):
                CM[(guard,t)] += 1
                C[guard] += 1

def argmax(d):
    best = None
    for k,v in d.items():
        if best is None or v > d[best]:
            best = k
    return best

best_guard, best_min = argmax(CM)
print best_guard, best_min

print best_guard * best_min
"""



""" #Fuck this shit.  The 3rd attempt at solving this below doesn't work.
#Trying this all overa gain

import re
import pandas as pd
import numpy as np
from scipy import stats

headerText = ['Date','Time','Text']
data = pd.DataFrame(columns=headerText)
with open('Inputs\Day4.input','r') as f:
    for line in f:
        tmp = re.split(r'\] | +', line[6:-1])
        data.loc[len(data)] = [tmp[0],tmp[1],tmp[3]]
data['Month'], data['Day'] = data['Date'].str.split('-').str
data['Hour'], data['Mins'] = data['Time'].str.split(':').str
data.sort(['Month', 'Day', 'Time'], inplace = True)
data.reset_index(inplace=True, drop=True)

# Thank you Pandas.  Now go through the data and find delta time
deltaTime = []
GuardID = []
for idx in range(len(data)):
    if idx == 0: #First line, seed with 0
        deltaTime.append(0)
    else:
        a = int(data['Mins'][idx])
        b = int(data['Mins'][idx-1])
        c = a-b
        if c < 0: #hour wraparound
            c = c + 60
        deltaTime.append(c) # Some of these are meaningless because they're on separate days, but whatever
    # seed GuardID
    skip = 0
    while data['Text'][idx - skip] in ['asleep','up']:
        skip += 1
    GuardID.append(data['Text'][idx - skip])

data['DeltaMins'] = deltaTime
data['GuardID'] = GuardID
print data.head()

# to find length of time asleep, we want to look at the DeltaMins in the rows labeled 'up'
# These will be the time since falling asleep, when the state changes to 'up'

sleepTimes = data['DeltaMins'].where(data['Text']=='up')
data['SleepTime'] = sleepTimes

uniqueGuard = data['GuardID'].unique()

maxSleep = 0
maxSleepGuardID = 0
for guard in uniqueGuard:
    a = data['SleepTime'].where(data['GuardID'] == guard).dropna().values
    totalsleep = a.sum()
    if totalsleep > maxSleep:
        maxSleep = totalsleep
        maxSleepGuardID = guard

# For the guard that sleeps the most, find most slept minute 
# I'm not sure the best way to do this, so I'm going to do it the ugly way

print maxSleep
print maxSleepGuardID

# Find the indicies where Text column has the correct Guard ID.
idx = data.index[data['Text'] == '#3203'].tolist()
minsAsleep = np.array([]) 
for i in idx:
    startSleep = -1
    endSleep = -1
    foundFlag = False
    counter = 1
    while not foundFlag:
        if data['Text'][i+counter] == 'asleep':
            startSleep = int(data['Mins'][i+counter])
            counter += 1
        if data['Text'][i+counter] == 'up':
            if startSleep > -1: # we've already found a valid sleep time
                endSleep = int(data['Mins'][i+counter])
                counter += 1
                foundFlag = True
        minsAsleep = np.append(minsAsleep, range(startSleep, endSleep))
        #minsAsleep = np.append(minsAsleep,range(int(startSleep), int(endSleep)))

print maxSleepGuardID
#print minsAsleep
print stats.mode(minsAsleep)
#print int(maxSleepGuardID.lstrip('#')) * stats.mode(minsAsleep)
"""
