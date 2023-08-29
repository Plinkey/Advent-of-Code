# Day 9

import intcode


with open('Day09.input','r') as f:
    data = [l.rstrip('\n') for l in f][0]
    
computer = intcode.intcode(data)
computer.execute()
computer.curInput = 1
computer.execute()
computer.curRecall

# Example
data = '109,19,204,-34,99'
computer = intcode.intcode(data)
computer.curBase = 2000
computer.program[1985] = 1111
computer.execute()
assert computer.curRecall == 1111


# Example Should print copy of itself.
data = '109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99'
computer = intcode.intcode(data)
computer.execute()

# Example Will output a sixteen-digit number
data = '1102,34915192,34915192,7,4,7,99,0'
computer = intcode.intcode(data)
computer.execute()
assert len(str(computer.curRecall)) == 16

# Example will output big number
data = '104,1125899906842624,99'
computer = intcode.intcode(data)
computer.execute()
assert computer.curRecall == 1125899906842624

# Test case from subreddit, should output -1
data = '109, -1, 4, 1, 99'
computer = intcode.intcode(data)
computer.execute()
assert computer.curRecall == -1


# Test case from subredit, should output +1
data  = '109, -1, 104, 1, 99'
computer = intcode.intcode(data)
computer.execute()
assert computer.curRecall == +1

# Test case from subreddit, should output 109
data = '109, -1, 204, 1, 99'
computer = intcode.intcode(data)
computer.execute()
assert computer.curRecall == 109

# Test case from subreddit, should output 204
data = '109, 1, 9, 2, 204, -6, 99'
computer = intcode.intcode(data)
computer.execute()
assert computer.curRecall == 204

# Test case from subreddit, should output 204
data = '109, 1, 109, 9, 204, -6, 99'
computer = intcode.intcode(data)
computer.execute()
assert computer.curRecall == 204

# Test case from subreddit, should output 204
data = '109, 1, 209, -1, 204, -106, 99'
computer = intcode.intcode(data)
computer.execute()
assert computer.curRecall == 204

# Test case from subreddit, should output input
data = '109, 1, 3, 3, 204, 2, 99'
computer = intcode.intcode(data)
a = 999
computer.execute()
computer.curInput = a
computer.execute()
assert computer.curRecall == a

# Test case from subreddit, should output input
data = '109, 1, 203, 2, 204, 2, 99'
computer = intcode.intcode(data)
a = 999
computer.execute()
computer.curInput = a
computer.execute()
assert computer.curRecall == a

# Example I made up.  program[7] should = 10+6 = 16
data = '109, 5,21101,10,6,2,99,0'
computer = intcode.intcode(data)
computer.execute()
assert computer.program[7] == 16

# Example I made up.  program[7]  should = 10+10
data = '1001, 5, 10, 7,99,10,0,0'
computer = intcode.intcode(data)
computer.execute()
assert computer.program[7] == 20


# Example I made up
data = '203,-5, 99,0'
computer = intcode.intcode(data)
computer.curBase = 5+3
computer.execute()
computer.curInput = 101
computer.execute()
assert computer.program[3] == 101


