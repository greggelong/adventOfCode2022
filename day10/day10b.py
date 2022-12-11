localpath="C:/Users/gkrei/Documents/adventOfCode2022/day10"

with open(localpath+'/sdata.txt') as f:
    dbuffer = f.readlines()

instr = [item.rstrip('\n') for item in dbuffer]

print(instr)

# after each cycle get a new sprite positon
def noopit():
    global cycle
    cycle+=1
    if cycle in [20,60,100,140,180,220]:
            print(cycle,x,cycle*x)
            signal.append(cycle*x)


def addx(strInstr):
    global x, cycle, oldx
     
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
    oldx = x
    x=x+int(lstInstr[1])
    if cycle in [20,60,100,140,180,220]:
        print(cycle,x, cycle*x)
        signal.append(cycle*x)


def getspritepos():
    global spl, sp , oldx, x
    ## set list to zero
    spl =[]
    print("old x ", oldx, " X ",x)
    sp = x
    spl.insert(sp,'#')
    spl.insert(sp+1,'#')
    spl.insert(sp+2,'#')
    print(cycle,spl, sp)
    oldx = x



x=1
oldx = x
cycle =1
sprite = '###'
signal = []
spl = []

sp = oldx - x
crtRow=[]
for i in instr:
    getspritepos()
    print(cycle,x)
    if i[0]=='n':
        noopit()
    else:
        addx(i) 

print(sum(signal))

    
