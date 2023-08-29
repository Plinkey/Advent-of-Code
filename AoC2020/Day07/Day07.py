debug = False


# %% Load Inputs
if debug:
    with open('Day07.example', 'r') as f:
        data = f.read().splitlines()
else:    
    with open('Day07.input', 'r') as f:
        data = f.read().splitlines()
        
"""
dark olive bags contain 3 faded blue bags, 4 dotted black bags.

<two word> bags contain <number> faded <two word>, <number> <two word> bags.

"""
# %% Parse input and load reqs
reqs = {}
for line in data:
    # bag = line.split(' ')[0:2]
    # bag = bag[0] + ' ' + bag[1]
    # req = line.
    splits = line.split('contain')
    bag = splits[0].rstrip(' bags ')
    rs = splits[1].split(',')
    rs = [r.strip().rstrip(',').rstrip('.') for r in rs]
    if rs[0] == 'no other bags':
        reqs[bag] = 'None'
        continue
#    sues[sueno] = {f.split(': ')[0].strip(): int(f.split(': ')[1]) for f in params}
    list_req = {}
    for r in rs:
        r = r.strip(' bag')
        r = r.strip(' bags')
        num, bagtype = r.split(' ',maxsplit=1)
        list_req[bagtype] = int(num)
    
    reqs[bag] = list_req
    
# %%
# Find all bags that contain a given color bag inside them
def findBagContents(inBag):
    answer = []
    for r in reqs:
        if inBag in reqs[r]:
            answer.append(r)
    return answer

# %%
# Recursion function to count
def countRecur(inBag):
    count = [b for b in findBagContents(inBag)]
    for new in findBagContents(inBag):
        a = countRecur(new)
        for aa in a:
            if aa not in count:
                count.append(aa)
    return count
        
print('The answer to part one is: {}'.format(len(countRecur('shiny gold'))))
# Answer is NOT 397.  answer < 397
# Answer is NOT 24.  Didn't tell me if it's too high or low
# Correct answer is 278

def numBagRecur(inBag):
    count = 0
    requirement = reqs[inBag]
    if requirement == 'None':
        return 0
    for r in requirement:
            n = requirement[r]
            count += n + n * numBagRecur(r)
    return count

print('The answer to part two is: {}'.format(numBagRecur('shiny gold')))
