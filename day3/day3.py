localpath="C:/Users/gkrei/Documents/adventOfCode2022/day3"

with open(localpath+'/sdata.txt') as f:
    dsacks = f.readlines()

#import dirty sacks dsacks and then strip \n  to get clean

sacks = [sack.rstrip('\n') for sack in dsacks]
#print(dsacks)
#print(sacks)