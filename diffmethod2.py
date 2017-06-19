# code as in diffmethod but do only arithmetic and use function

import sys

seqin = raw_input("Please enter the first few terms of your sequence separated by ',' ").split(",")
seqin = map(int, seqin)
#print "The length of your string is: ", len(n)

while len(seqin) % 2 != 0:
    print "Could you re-enter the sequence, given an even number of terms?" 
    seq = raw_input("Please enter the first few terms of your sequence separated by ',' ").split(",")
    seq = map(int, n)

print "Great, this is a good sequence."

    
def generatef(seq):
    diff1 = [None] * (len(seq)-1)

    for i in range(len(seq)-1): 
        diff1[i] = seq[i+1] - seq[i]
    c = 0

    seqminusn2 = [None] * (len(seq))

    if (diff1[0] == diff1[1] and diff1[1] == diff1[2] and diff1[0] < 0):
        print "This is an arithmetic sequence, it decreases by a factor", diff1[0], "at each step."
        c = - diff1[0]*1 + seq[0]
        print "the formula generating such sequence is An = ", diff1[0], "n +", c 
    elif (diff1[0] == diff1[1] and diff1[1] == diff1[2] and diff1[0] >= 0):
        c = - diff1[0]*1 + seq[0]
        print "This is an arithmetic sequence, it increases by a factor", diff1[0], "at each step."
        print "the formula generating such sequence is An = ", diff1[0], "n +", c 
    else: 
        print "This may be a geometric sequence."

print generatef(seqin)

'''
diff1 = [None] * (len(seq)-1)

for i in range(len(seq)-1): 
    diff1[i] = seq[i+1] - seq[i]

diff2 = [None] * (len(seq)-2)

for i in range(len(seq)-2): 
    diff2[i] = diff1[i+1] - diff1[i]

c = 0

seqminusn2 = [None] * (len(seq))

if (diff1[0] == diff1[1] and diff1[1] == diff1[2] and diff1[0] < 0):
    print "This is an arithmetic sequence, it decreases by a factor", diff1[0], "at each step."
    c = - diff1[0]*1 + seq[0]
    print "the formula generating such sequence is An = ", diff1[0], "n +", c 
elif (diff1[0] == diff1[1] and diff1[1] == diff1[2] and diff1[0] >= 0):
    c = - diff1[0]*1 + seq[0]
    print "This is an arithmetic sequence, it increases by a factor", diff1[0], "at each step."
    print "the formula generating such sequence is An = ", diff1[0], "n +", c 
else: 
    print "This may be a geometric sequence."
    if diff2[0] == diff2[1] and diff2[1] == diff2[2]:
        print "We checked, this is ACTUALLY a geometric sequence."
        for i in range(len(seq)):
            seqminusn2[i] = seq[i] - (((i+1)**2)*(diff2[0] / 2))
#((i+1)**2)*(diff2[0]/6)               
        print seqminusn2
        print "I still need to finish this code from here."
    else:
        print "Sorry, we checked. This is NOT a geometric sequence. We can't help you any longer."
        sys.exit(0)
                
Code again by defining an arithmetic function

def greater_less_equal_5(answer):
    if answer > 5:
        return 1
    elif answer < 5:          
        return -1
    else:
        return 0
        
print greater_less_equal_5(4)

def diffari(seqin)
'''
