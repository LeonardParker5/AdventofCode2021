commandlist = []

with open('Resources/day2input.txt') as f:
    for line in f:
        commandlist.append(line.rstrip())
    
#PART 1
x = 0
y = 0

for i in commandlist:
    isplit = i.split(" ")
    if(isplit[0] == "forward"):
        x += int(isplit[1])
    if(isplit[0] == "up"):
        y -= int(isplit[1])
    if(isplit[0] == "down"):
        y += int(isplit[1])

print("x: " + str(x) + "\n" + "y: " + str(y) + "\n" + "total: " + str((x * y)))

#PART 2
x = 0
y = 0
aim = 0

for i in commandlist:
    isplit = i.split(" ")
    if(isplit[0] == "forward"):
        #change horizontal by value
        x += int(isplit[1])
        #change depth by aim
        y += (int(isplit[1]) * aim)
    if(isplit[0] == "up"):
        aim -= int(isplit[1])
    if(isplit[0] == "down"):
        aim += int(isplit[1])

print("x: " + str(x) + "\n" + "y: " + str(y) + "\n" + "total: " + str((x * y)))