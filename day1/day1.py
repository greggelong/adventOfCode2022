localpath="C:/Users/gkrei/Documents/adventOfCode2022/day1"

with open(localpath+'/data.txt') as f:
    lines = f.readlines()

# make the dictionary
elves ={}
elf =1
cals =[]
for item in lines:
    elves[elf] = cals
    if item != '\n':
        elves[elf].append(int(item))
    else:
        elf=elf+1
        cals =[]


#print(elves)

#print(elves.values())

## just get a list of values
callist = list(elves.values())        
#print(sum(callist[0]))  

most =0
myelf =0
for elf, cal in enumerate(callist):
    if most < sum(cal):
        most = sum(cal)
        myelf = elf

print(myelf+1, most) # +1 because elves start with 1 not zero        


## a better way to use dictionary with key value items

most =0
myelf =0
for key, value in elves.items():
    if most < sum(value):
        most= sum(value)
        myelf = key   

print("key value items: ", myelf, most) # dont need 

## part 2

## make a dict with summed values

sumelves = {k:sum(v) for k,v in elves.items()  }

#print(sumelves)

# get values as a list
sumCalList = list(sumelves.values())

#print(sumCalList)
# sort that list from most to least
sumCalList.sort(reverse=True)

#print(sumCalList)

# total the top 3
total = sumCalList[0]+sumCalList[1]+sumCalList[2]

print("top three elves", total)