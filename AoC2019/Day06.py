
#class planet:
#    def __init__(self, code):
#        parent, child = code.split(')')
#        self.parent = parent
#        self.child = child
#        
#        
#Raw_Test = "COM)B,B)C,C)D,D)E,E)F,B)G,G)H,D)I,E)J,J)K,K)L"
#data = [l.split(')') for l in Raw_Test.split(',')]
with open('Day06.input','r') as file:
    raw_data = file.read().strip()
data = [l.split(')') for l in raw_data.split('\n')]    
parent={}



for orbit in data:
    parent[orbit[1]] = orbit[0]


path = {}

def getPath(object):
        nextPlanet = parent[object]
        if nextPlanet == 'COM': # Final orbit
            return 1
        else:
            return 1 + getPath(nextPlanet)

for i in parent.keys():
    path[i] = getPath(i)

print('answer part 1 = ' + str(sum(path.values())))


######
# Part 2
#####

myPath = ['YOU']
santaPath = ['SAN']

while myPath[-1] != 'COM':
    # Trace path all the way back to COM, [-1] is always the end
    myPath.append(parent[myPath[-1]])
    
while santaPath[-1] != 'COM':
    # Trace path all the way back to COM [-1] is alwyas the end
    santaPath.append(parent[santaPath[-1]])

while santaPath[-1] == myPath[-1]: #starting from the end, find ==
    # Finds the first intersection of orbital transfers.
    # This will keep popping the last element until the paths diverge
    # starts at COM and works its way forward
    santaPath.pop() #remove last element
    myPath.pop()
    
print('Part 2 answer = '+str(len(myPath)+len(santaPath)-2))
