import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'data')

file = open(filename, 'r')
lines = file.readlines()

sumArray = []
sumArray.append(0)
count = 0
for line in lines:
    line = line.strip()
    if line=="":
        count += 1
        sumArray.append(0)
    else:
        sumArray[count] += int(line)

print(max(sumArray))
