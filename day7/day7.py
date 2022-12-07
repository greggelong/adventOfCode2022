
# for part one I dont think i need recursion

## oh no directorys at different levels have the same names a dictiona

localpath="C:/Users/gkrei/Documents/adventOfCode2022/day7"

with open(localpath+'/sdata.txt') as f:
    dtermOutput= f.readlines()

termOutput = [item.rstrip('\n') for item in dtermOutput]

print(termOutput)


## get a list of all the directories

dirlist =[]
for item in termOutput:
    itemList = item.split(" ")
    if itemList[0] == "dir":
        dirlist.append(itemList[1])


print(dirlist)

## make a dictionary of all key = directory and value = total size

dirdict = {}
for d in dirlist:
    total = 0
    print(d)
    ## go through all the term output looking for item that matches the list of directories 
    for item in termOutput:
       # print("item: ",item)
        itemList = item.split(" ")
        #print(itemList)
        if len(itemList) >1 and itemList[1] == "cd" and itemList[2] == d:  #$ cd a # also need to account for shorter lists with first condition
            #print("bing")
            myindex = termOutput.index(item)+2 # skip over the ls
            #print(myindex)
            #print(termOutput[myindex])
            while termOutput[myindex][0] != "$":
                #print("entered while")
                 
                checkifnum = termOutput[myindex].split(" ")
                if checkifnum[0].isnumeric():
                    #print("add it")
                    total += int(checkifnum[0])
                    #print(total)
                if termOutput[myindex] == "eof":
                    break
                myindex+=1
    dirdict[d]= total
    


print(dirdict)


## find witch directories are in in other directories
collapseTotals =[]
collapse =[]
for d in dirlist:
    total = [d]
    total1 =dirdict[d]
    ## put in totals:
    for item in termOutput:
           # print("item: ",item)
        itemList = item.split(" ")
        #print(itemList)
        if len(itemList) >1 and itemList[1] == "cd" and itemList[2] == d:  #$ cd a # also need to account for shorter lists with first condition
            #print("bing")
            myindex = termOutput.index(item)+2 # skip over the ls
            #print(myindex)
            #print(termOutput[myindex])
            while termOutput[myindex][0] != "$":
                #print("entered while")
                 
                checkifdir = termOutput[myindex].split(" ")
                if checkifdir[0]== 'dir':
                    #print("add it")
                    if checkifdir[1] not in total:
                        total.append(checkifdir[1])
                        total1 += dirdict[checkifdir[1]]
                    #print(total)
                if termOutput[myindex] == "eof":
                    break
                myindex+=1

    collapseTotals.append(total1)
    collapse.append(total)

print("collapse", collapse)   
print(collapseTotals) 


sum =0
for n in collapseTotals:
    if n <= 100000:
        sum+=n
        


print(sum)

