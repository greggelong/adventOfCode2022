localpath="C:/Users/gkrei/Documents/adventOfCode2022/day10"

with open(localpath+'/sdata.txt') as f:
    dbuffer = f.readlines()

instr = [item.rstrip('\n') for item in dbuffer]

print(instr)


def noopit():
    global cycle
    cycle+=1
    if cycle in [20,60,100,140,180,220]:
            print(cycle,x,cycle*x)
            signal.append(cycle*x)


def addx(strInstr):
    global x, cycle
     
    lstInstr = strInstr.split(' ')
    #print(int(lstInstr[1]))
    #take two cycles
    cycle+=1
    if cycle in [20,60,100,140,180,220]:
        print(cycle,x, cycle*x)
        signal.append(cycle*x)
        #rangnumb.remove(cycle)

    #after two cycles update x
   
    cycle+=1
    x=x+int(lstInstr[1])
    if cycle in [20,60,100,140,180,220]:
        print(cycle,x, cycle*x)
        signal.append(cycle*x)




x=1
cycle =1
sprite = '###'
signal = []

sprite_pos = sprite+'.'*(40-3)
crtRow=[]
for i in instr:
    #print(cycle,x)
    if i[0]=='n':
        noopit()
    else:
        addx(i) 

print(sum(signal))

    
