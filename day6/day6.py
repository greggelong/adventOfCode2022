s1 ="mjqjpqmgbljsphdztnvjfqwrcgsmlb"
s2 ="bvwbjplbgvbhsrlpgdmjqwftvncz"
s4 ="nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
s5 ="zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"

localpath="C:/Users/gkrei/Documents/adventOfCode2022/day6"

with open(localpath+'/data.txt') as f:
    dbuffer = f.readlines()

buffer = [item.rstrip('\n') for item in dbuffer]

print(buffer)



l1 = list(buffer[0])
#l1 = list(s1)

print(l1)

# make a bucket of 4 then check that bucket with a set of that bucket
# sets will get rid of duplicates 
# if the len of set and len of  list are the same we have found the marker

#start of packet marker 
for i in range(len(l1)-4):
    bucket = [l1[i],l1[i+1], l1[i+2],l1[i+3]]
    ## check for duplicates with set
    if len(set(bucket)) == len(bucket):
        print(i+4,l1[i], bucket)
        break


#start of message marker

for i in range(len(l1)-14):
    bucket =[]
    for j in range(14):
        bucket.append(l1[i+j])
        #print(bucket)
         ## check for duplicates with set
        
    if len(set(bucket)) == len(bucket):
        print(i+14,l1[i], bucket)
        break
    