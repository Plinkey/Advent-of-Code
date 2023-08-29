debug = False

if debug:
    with open('Day06.example', 'r') as f:
        data = f.read().split('\n\n')
else:
    with open('Day06.input', 'r') as f:
        data = f.read().split('\n\n') 
        
        
# %%
# Count unique in string
def countUnique(string):
    a = set(string)
    if '\n' in a:
        a.discard('\n')
    return len(a)
    
total = 0
for group in data:
    total += countUnique(group)
    
print('The answer to part one is: {}'.format(total))

# %% 
# Part 2
def countAll(string):
    a = string.split('\n')
    aa = set(a[0])
    for n in a[1:]:
        aa = aa.intersection(n)
    return len(aa)
    
total = 0
for group in data:
    total += countAll(group)


print('The answer to part two is: {}'.format(total))