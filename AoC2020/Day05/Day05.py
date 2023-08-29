with open('Day05.input', 'r') as f:
    data = f.read().splitlines()
    

def row(instr):
    row = 0
    for idx in range(7):
        if instr[idx] == 'B':
            v = 1
        else:
            v = 0
        row += v * 2**(6-idx)
    return row
        
""" 
0 1     
1 2
2 4
3 8
4 16
5 32
6 64
B's = 1
F's = 0
"""

def column(instr):
    column = 0
    code = instr[-3:]
    # print(code)
    for idx in range(3):
        if code[idx] == 'R':
            v = 1
        else:
            v = 0
        column += v * 2**(2-idx)
    return column

"""
0 1
1 2
3 4
"""

def seat(instr):
    return row(instr) * 8 + column(instr)

maximum = 0
for item in data:
    maximum = max(maximum, seat(item))

print('The answer to part one: {}'.format(maximum))
    
    
# %%
# Part 2

tot = []
for item in data:
    tot.append(seat(item))
    
everything = list(range(max(tot)))
missing = set(everything).difference(tot)
print('The answer to part two: {}'.format(max(missing)))

# This gives the correct answer.  I'm not sure why on part 2...