localpath="C:/Users/gkrei/Documents/adventOfCode2022/day4"

with open(localpath+'/sdata.txt') as f:
    dpairs = f.readlines()

#import dirty sacks dsacks and then strip \n  to get clean

pairs = [pair.rstrip('\n') for pair in dpairs]


#print(pairs)

totalcontain =0 ## to hold pairs that fully conatain each other 
totaloverlap =0
for pair in pairs:
    # split pairs
    splitpair = pair.split(',')
    #print(splitpair)
    ## get ranges
    range1 = splitpair[0].split('-')
    range2 = splitpair[1].split('-')
    print(splitpair, range1,range2)
    
    ## get 
    r1begin = int(range1[0])
    r1end = int(range1[1])
    r2begin = int(range2[0])
    r2end = int(range2[1])
    
    #contain 
   # if r1begin >=r2b
    
print("total contain",totalcontain)
print("total overlap",totaloverlap)

## my first try was making a string of the numbers instead of a list but ran in to trouble because
## the range 2-3  would be identical to to the range 23-23 like that
## but it could have been solved with adding a character to the string such as a "." so 2.3. would be different from 23.

