file = open('data', 'r')
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
