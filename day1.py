depthlist = []

with open('Resources/day1input.txt') as f:
    for line in f:
        depthlist.append(int(line.rstrip()))

#PART 1

depthcounter = 0
for i in range(len(depthlist) - 1):
    if(depthlist[i + 1] > depthlist[i]):
        depthcounter += 1

print("depthcounter is " + str(depthcounter))

#PART 2

groupcounter = 0
for i in range(len(depthlist) - 3):
    blockA = (depthlist[i] + depthlist[i + 1] + depthlist[i + 2])
    blockB = (depthlist[i + 1] + depthlist[i + 2] + depthlist[i + 3])
    if(blockB > blockA):
        groupcounter += 1
    
print("groupcounter is " + str(groupcounter))
