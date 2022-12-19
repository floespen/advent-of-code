import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'data')

file = open(filename, 'r')
lines = file.readlines()

resultSet = []
for line in lines:
    line = line.strip()
    lengthOfLine = len(line)
    first = line[0 : int(lengthOfLine/2)]
    first = line[0 : int(lengthOfLine/2)]
    second = line[int(lengthOfLine/2) : int(lengthOfLine)]
    print(line)
    print(first)
    print(second) 
    listOfEquality = []
    for charFirst in first:
        for charSecond in second:
            if charFirst == charSecond and len(listOfEquality)==0:
                listOfEquality.append(charFirst)
    print(listOfEquality)
    ordinary = ord(listOfEquality[0].swapcase())-64
    if ordinary > 26:
        ordinary = ordinary - 6
    print(ordinary)
    resultSet.append(ordinary)

    print(sum(resultSet))
