class Monkey:
    def __init__(self, name,items, opert,test,iftrue,iffalse):
        self.name = name
        self.items = items
        self.opert = opert
        self.test = test
        self.iftrue = iftrue
        self.iffalse = iffalse

    def __str__(self):
        return f"{self.name}({self.items},{self.opert},{self.test},{self.iftrue},{self.iffalse})"

        ## for operation use string and eval(string)

    def turn(self):
        print("Monkey: ",self.name)
        print(type(self.items))
        i = 0;
        while len(self.items)>0:
            monkeyInspectedItems[self.name]+=1
            print("list size", len(self.items))
            old = self.items.pop(0)
            new  = eval(self.opert) 
            print(i, old)
            print("eval: ",new)
            new = int(new/3)
            print("divide by 3", new)
            if new%self.test == 0:
                mlist[self.iftrue].items.append(new)
                print("throw to monkey ", self.iftrue)
            else:
                mlist[self.iffalse].items.append(new)
                print("throw to monkey ", self.iffalse)
            i+=1
            print(len(self.items))





m0= Monkey(0,[79,98],"old * 19",23,2,3)
m1= Monkey(1,[54,65,75,74],"old +6",19,2,0)
m2= Monkey(2,[79,60,97],"old * old",13,1,3)
m3= Monkey(3,[74],"old + 3",17,0,1)

mlist =[m0,m1,m2,m3]

monkeyInspectedItems =[0,0,0,0]

for i in range(20):
    print(i)
    for m in mlist:
        m.turn()


for m in mlist:
    print(m)

print(monkeyInspectedItems)
monkeyInspectedItems.sort(reverse=True)
print(monkeyInspectedItems[0]*monkeyInspectedItems[1])