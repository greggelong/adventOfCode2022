localpath="C:/Users/gkrei/Documents/adventOfCode2022/day13"

with open(localpath+'/sdata.txt') as f:
    dpackets = f.readlines()

packets = [item.rstrip('\n') for item in dpackets]

print(packets)

list1 = eval(packets[0])
list2 = eval(packets[1])

print(list1,list2, type(list1))

## I can use eval to read the data in as a list no need to rebuild them

