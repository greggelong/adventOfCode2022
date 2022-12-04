localpath="C:/Users/gkrei/Documents/adventOfCode2022/day2"

with open(localpath+'/rpsData.txt') as f:
    tournament = f.readlines()


print(tournament)

## if in rock paper or scissors
rock = ["A","X"]
paper = ["B", "Y"]
scissors = ["C","Z"]

# part 1

total =0
for round in tournament:
    opp = round[0]
    me = round[2]
    #tie
    if opp in rock and me in rock or opp in paper and me in paper or opp in scissors and me in scissors:
        if me in rock:
            total = total + 4 # 1 rock + 3 draw
        elif me in paper:
            total = total + 5 # 2 paper + 3 draw
        elif me in scissors:
            total = total +6 #3 sci +3 draw
    # win
    elif me in paper and opp in rock or me in rock and opp in scissors or me in scissors and opp in paper:
        if me in rock:
            total = total + 7 # 1 rock + 6 win
        elif me in paper:
            total = total + 8 # 2 paper + 6 win
        elif me in scissors:
            total = total + 9 #3 sci + 6 win
    #lose
    else:
        if me in rock:
            total = total + 1# 1 rock + 0 lose
        elif me in paper:
            total = total + 2 # 2 paper + 0 lose
        elif me in scissors:
            total = total + 3 #3 sci + 0 lose

print(total)



# part 2
total =0

for round in tournament:
    outcome = round[2]
    opp= round[0]
    #tie
    if outcome == "Y":
        if opp in rock:
            total = total + 4 # 1 rock + 3 draw
        elif opp in paper:
            total = total + 5 # 2 paper + 3 draw
        elif opp in scissors:
            total = total +6 #3 paper +3 draw
    #win
    elif outcome == "Z":
        if opp in rock:
            total = total + 8 # 2 paper + 6 win
        elif opp in scissors:
            total = total + 7 # 1 rock + 6 win
        elif opp in paper:
            total = total + 9 #3 paper + 6 win
    #lose
    elif outcome == "X":
        if opp in rock:
            total = total + 3 #3 sci + 0 lose
        elif opp in paper:
            total = total + 1# 1 rock + 0 lose
        elif opp in scissors:
            total = total + 2 # 2 paper + 0 lose

print(total)




