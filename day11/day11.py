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





m0= Monkey(0,[52,60,85,69,75,75],"old * 17",13,6,7)
m1= Monkey(1,[96,82,61,99,82,84,85],"old + 8",7,0,7)
m2= Monkey(2,[95,79],"old + 6",19,5,3)
m3= Monkey(3,[88,50,82,65,77],"old * 19",2,4,1)
m4= Monkey(4,[66,90,59,90,87,63,53,88],"old +7",5,1,0)
m5= Monkey(5,[92,75,62],"old * old",3,3,4)
m6= Monkey(6,[94,86,76,67],"old + 1",11,5,2)
m7= Monkey(7,[57],"old + 2",17,6,2)

mlist =[m0,m1,m2,m3,m4,m5, m6, m7]

monkeyInspectedItems =[0,0,0,0,0,0,0,0]

for i in range(20):
    print(i)
    for m in mlist:
        m.turn()


for m in mlist:
    print(m)

print(monkeyInspectedItems)
monkeyInspectedItems.sort(reverse=True)
print(monkeyInspectedItems[0]*monkeyInspectedItems[1])