inputlist = []

with open('Resources/day3input.txt') as f:
    for line in f:
        inputlist.append(line.rstrip())

#PART 1
#initialize list
powerlist = []
for i in range(0, len(inputlist[0])):
    powerlist.append(0)

#determine gamma count
for i in inputlist:
    for j in range(0, len(i)):
        if i[j] == "1":
            powerlist[j] += 1
        else:
            powerlist[j] -= 1
        
#determine gamma binary
for i in range(0, len(powerlist)):
    if powerlist[i] > 0:
        powerlist[i] = 1
    else:
        powerlist[i] = 0

gamma = ''.join([str(int) for int in powerlist])
epsilon = ''.join('1' if x == '0' else '0' for x in [str(int) for int in powerlist])

print("power consumption is " + str((int(gamma,2)) * (int(epsilon,2))))
