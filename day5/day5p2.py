localpath="C:/Users/gkrei/Documents/adventOfCode2022/day5"

with open(localpath+'/sdata.txt') as f:
    dinstr= f.readlines()

#import dirty sacks dsacks and then strip \n  to get clean

instr= [instr.rstrip('\n') for instr in dinstr]

## to solve this I have to write a language interpreter 

#print(instr)

# part 2


smallStack = [[],['Z','N'],['M','C','D'],['P']]

bigStack =[[],['R','P','C','D','B','G'],['H','V','G'],['N','S','Q','D','J','P','M'],['P','S','L','G','D','C','N','M'],['J','B','N','C','P','F','L','S'],['Q','B','D','Z','V','G','T','S'],['B','Z','M','H','F','T','Q'],['C','M','D','B','F'],['F','C','Q','G']]


def make_move(stacks,nt,fs,ts):
    '''stack 2d lists, number of moves, from stack, to stack'''
    take = stacks[fs][len(stacks[fs])-nt:] ## get the number of boxes off the stack
    del stacks[fs][len(stacks[fs])-nt:]  ## delete those
    stacks[ts].append(take)   ## append them to the to stack
    #print(smallStack)


for item in instr:
    instrL = item.split(" ")
    #print(instrL)
    nTimes = int(instrL[1])
    fromStack = int(instrL[3])
    toStack = int(instrL[5])
    make_move(smallStack,nTimes,fromStack,toStack)

#print(bigStack[1][-1],bigStack[2][-1],bigStack[3][-1])

for i in range(1,len(smallStack)):
    print(i,smallStack[i][-1])


# part 2 special crane moves more  reset 

