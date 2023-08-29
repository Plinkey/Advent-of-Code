""" Advent of Code 2018 Day 5"""

with open('Inputs\Day5.input', 'r') as f:
    data = f.read()

doneFlag = False

#curStr = 'foObaAr'
# creating a function for part 2
def React(curStr):
    doneFlag = False
    while not doneFlag:
        doneFlag = True # Reset this now, if it passes through whole polymer and finds nothing
                        # Then it'll end the infinite loop
        for idx in range(len(curStr)):
            #print idx
            #print curStr[idx]
            if idx == len(curStr)-1: #this is the last item, there is nothing next
                #print 'nothing found idx==len(curStr)'
                break
            elif curStr[idx].lower() == curStr[idx+1].lower(): # if characters are the same
                if curStr[idx].isupper() != curStr[idx+1].isupper():# opposite polarity
                    #print 'snipping'
                    newStr = curStr[:idx] + curStr[idx+2:]
                    curStr = newStr
                    doneFlag = False
                    break
    return curStr


print len(React(data))



#########
# Part 2
#########

# Find unique characters

unique = ''.join(set(data.lower()))

def Remove(curStr,char):
    # Replace both lower and uppercase
    newStr = curStr.replace(char.lower(),"")
    newStr = newStr.replace(char.upper(),"")
    return newStr

polymerCount = {}
for letter in unique:
    print 'working letter %s' %letter
    newStr = Remove(data,letter)
    polymerCount[letter] = len(React(newStr))

print min(polymerCount.values())
