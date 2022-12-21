import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'data')

file = open(filename, 'r')
lines = file.readlines()
counter = 0

for line in lines:
    line = line.strip()
    left, right = line.split(',')
    leftPair = left.split('-')
    rightPair = right.split('-')

    print(line)
    print(leftPair)
    print(rightPair)

    if (int(leftPair[0]) >= int(rightPair[0]) and int(leftPair[1]) <= int(rightPair[1])) or \
       (int(rightPair[0]) >= int(leftPair[0]) and int(rightPair[1]) <= int(leftPair[1])):
        counter = counter + 1
        print(1)
        print(counter)

print("counter: " + str(counter))
