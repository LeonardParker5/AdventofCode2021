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