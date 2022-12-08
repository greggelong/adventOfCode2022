
# for part one I dont think i need recursion

## oh no directorys at different levels have the same names a dictiona

localpath="C:/Users/gkrei/Documents/adventOfCode2022/day7"

with open(localpath+'/sdata.txt') as f:
    dtermOutput= f.readlines()

termOutput = [item.rstrip('\n') for item in dtermOutput]

termOutList =[item.split() for item in termOutput]
print(termOutput)

print(termOutList)


stack = []
sizes = []

def up():
    print("size", sizes)
    print("stack", stack)
    sizes.append(stack.pop(-1))
    if stack:
        stack[-1] += sizes[-1]

for line in termOutList:
    if len(line) >2 and line[0] == "$" and line[1] =="cd" and line[2] == ".." : up()
    elif len(line)  >2 and line[0] == "$" and line[1] == "cd" :stack.append(0)
    elif line[0]== "$": pass
    elif line[0]=="dir":pass
    elif line[0].isnumeric() :stack[-1]+=int(line[0])

       
while stack:
    up()

print(sum(s for s in sizes if s <= 100000))
print(min(s for s in sizes if s >= (max(sizes) - 40000000)))

