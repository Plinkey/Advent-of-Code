# Day 22



class deck:
    def __init__ (self, example=False):
        if example:
            self.nCards = 10
        else:
            self.nCards = 10007
        self.deck = list(range(self.nCards))

    def deal_new(self):
        self.deck.reverse()

    def cut_deck(self,n):
        self.deck = self.deck[n:]+self.deck[0:n]

    def deal_increment(self,n):
        new = [None] * self.nCards
        new_idx = 0
        for card in self.deck:
            new[new_idx] = card
            new_idx += n
            new_idx %= self.nCards
        self.deck = new


def process(filename):
    with open(filename,'r') as f:
        lines = [l.rstrip('\n') for l in f]
    if 'Example' in filename:
        a = deck(example=True)
    else:
        a = deck()
    for line in lines:
        if line == "deal into new stack":
            a.deal_new()
        elif line.startswith("cut"):
            n = int(line.split(' ')[-1])
            a.cut_deck(n)
        elif line.startswith("deal with increment"):
            n = int(line.split(' ')[-1])
            a.deal_increment(n)
    return a


# Example 1
assert process('Day22/Example1.input').deck == [0, 3, 6, 9, 2, 5, 8, 1, 4, 7]

# Example 2
assert process('Day22/Example2.input').deck == [3, 0, 7, 4, 1, 8, 5, 2, 9, 6]

# Example 3
assert process('Day22/Example3.input').deck == [6, 3, 0, 7, 4, 1, 8, 5, 2, 9]

# Example 4
assert process('Day22/Example4.input').deck == [9, 2, 5, 8, 1, 4, 7, 0, 3, 6]

tt = process('Day22/Day22.input')
print("Your answer is: "+str(tt.deck.index(2019))) 
