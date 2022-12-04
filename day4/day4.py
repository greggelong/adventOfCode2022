localpath="C:/Users/gkrei/Documents/adventOfCode2022/day4"

with open(localpath+'/data.txt') as f:
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
    #print(splitpair, range1,range2)
    
    ## create list of ranges
    listA =[]
    listB=[]
    for n in range(int(range1[0]),int(range1[1])+1):
        listA.append(str(n))
    for n in range(int(range2[0]),int(range2[1])+1):
        listB.append(str(n))
    #print(listA)
    #print(listB)
    ## check if a subrange using all and any for overlap
    if all(x in listA for x in listB) or all(x in listB for x in listA):
        totalcontain+=1
        #print(total)
    if any(x in listA for x in listB) or any(x in listA for x in listB):
        totaloverlap+=1
    ''' # sets not working 
    ## will try sets 
    if set(range(int(range1[0]), int(range1[1]))).issubset(range(int(range2[0]), int(range2[1]))) or set(range(int(range2[0]), int(range2[1]))).issubset(range(int(range1[0]), int(range1[1]))) :
        total+=1
        print(total,splitpair, range1,range2)
        #print(range(int(range1[0]), int(range1[1])), (range(int(range2[0]), int(range2[1]))))
        #print("bing")

    #print(range(int(range1[0]), int(range1[1])), (range(int(range2[0]), int(range2[1]))))
    '''
print("total contain",totalcontain)
print("total overlap",totaloverlap)

