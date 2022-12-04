localpath="C:/Users/gkrei/Documents/adventOfCode2022/day3"

with open(localpath+'/data.txt') as f:
    dsacks = f.readlines()

#import dirty sacks dsacks and then strip \n  to get clean

sacks = [sack.rstrip('\n') for sack in dsacks]
#print(dsacks)
#print(sacks)

## make a lookup table for priorities using a list made from string index of letter is priority
priorityStr = "0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

priority =list(priorityStr)
#print(priority)
#print(priority.index('p'))

total = 0
for sack in sacks:
    # split sacks in half
    sack1s = sack[:-int(len(sack)/2)]
    sack2s = sack[int(len(sack)/2):]
    # make into a list
    sack1 = list(sack1s)
    sack2 = list(sack2s)
    ## check for duplicates
    for item in sack1:
        if item in sack2:
            #if in sack to add the priority
            total= total+ priority.index(item)
            print(item)
            break ## only need to find 1

print(total)

