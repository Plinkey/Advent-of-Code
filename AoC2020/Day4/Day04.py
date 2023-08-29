with open('Day04.input', 'r') as f:
    data = f.read().splitlines()

#---------
# Examples
#---------
# with open('Day04.example', 'r') as f:
#     data = f.read().splitlines()
# with open('Day04pt2_invalid.example', 'r') as f:
#     data = f.read().splitlines()
# with open('Day04pt2_valid.example', 'r') as f:
#     data = f.read().splitlines()

"""
byr : birth year
iyr : Issue year
eyr : expiry year
hgt : height
hcl : hair color
ecl : eye color
pid : passport ID
cid : country ID

Everything but CID is required
# blank lines starts new entry
# if line == '': starts new entry

"""

validTags = ['byr','iyr','eyr','hgt','hcl','ecl','pid']


passportData = {}


# Parse Data
count = 1
passportData[1] = {}
for line in data:
    if line == '': # start new entry
        count += 1
        passportData[count] = {}
        continue
    info = line.split(' ')
    for i in info:
        tag, value = i.split(':')
        passportData[count][tag] = value
        

# Part 1 Validation
def validate(passport):
    if all(elem in passport.keys() for elem in validTags): # if validTags are present
        return True
    else:
        return False
    
# Count part 1 valid passports
validcount = 0
for p in passportData:
    if validate(passportData[p]):
        validcount += 1

print(validcount)
        

#-------
# Part two
#--------


# Part 2 validation
def validate2(passport):
    if not validate(passport):
        return False
    byr = passport['byr']
    iyr = passport['iyr']
    eyr = passport['eyr']

    hgt = passport['hgt']
    try: num = int(hgt[:-2])
    except: return False
    unit = hgt[-2:]
    # unit = hgt[3:]

    hcl = passport['hcl']
    ecl = passport['ecl']
    pid = passport['pid']

    if not(1920 <= int(byr) <= 2002) or len(byr) != 4:
        return False

    elif not(2010 <= int(iyr) <= 2020) or len(iyr) != 4:
        return False

    elif not(2020 <= int(eyr) <= 2030) or len(eyr) != 4:
        return False


    elif unit not in ['in','cm']:
        return False
    elif unit.lower() == 'in' and not(59<= num <= 76):
        return False
    # elif unit.lower() == 'in':
    #     if not(59<= num <= 76):
    #         return False
    elif unit.lower() == 'cm' and not(150<= num <= 193):
        return False
    # elif unit.lower() == 'cm':
    #     if not(150<= num <= 193):
    #         return False
    

    elif hcl[0] != '#' or len(hcl) != 7:
        return False

    elif ecl not in ['amb','blu','brn','gry','grn','hzl','oth']:
        return False

    elif len(pid) != 9:
        return False
    
    else:
        return True

pCount = 0
for p in passportData:
    if validate2(passportData[p]):
        pCount += 1

print(pCount)

