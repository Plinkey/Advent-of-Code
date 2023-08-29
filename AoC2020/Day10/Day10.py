from itertools import combinations

# %% Example 1
with open('Day10.example1','r') as f:
    data = f.read().splitlines()
    data = [int(i) for i in data]
    data.sort()

# %% Example 2
with open('Day10.example2','r') as f:
    data = f.read().splitlines()
    data = [int(i) for i in data]
    data.sort()

# %% Input
with open('Day10.input','r') as f:
    data = f.read().splitlines()
    data = [int(i) for i in data]

# %% Part 1
device = max(data)+3
curJolts = 0
part2list = []
counts = {1:0, 2:0, 3:0}

while True:
    if data == []:
        delta = device - curJolts
        counts[delta] += 1
        part2list.append(delta)
        break
    next_adapt = data.pop(data.index(min(data)))
    delta = next_adapt - curJolts
    counts[delta] += 1
    part2list.append(delta)
    curJolts = next_adapt
    
print('The answer to part one is: {}'.format(counts[1]*counts[3]))

# %% Part 2

# count = 0
# curJolts = 0

# while True:
#     if data == []:
#         delta = device - curJolts
        

# for i in range(2, len(data)):
#     for c in combinations(data, i):
#         if max(c) >= device - 3:
#             count += 1
#         else:
#             continue
        
# %% func
# It's getting to hard.  Had to consult reddit a bit to get me through.

def findIt(d):
    temp_list = []
    mult_list = []
    for n in d:
        if n != 3:
            temp_list.append(n)
        
        elif n == 3:
            if len(temp_list) > 3:
                mult_list.append((len(temp_list)-1)*2+(len(temp_list)-3))
            elif len(temp_list) > 1:
                mult_list.append((len(temp_list)-1)*2)
            temp_list = []
            
    r2 = 1
    for x in mult_list:
            r2 = r2 * x 
    return r2

print('The Answer to part two is: {}'.format(findIt(part2list)))