import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'data')

file = open(filename, 'r')
lines = file.readlines()

wtf = False
pointsCounter = 0

for line in lines:
    opponent, own = line.split(" ")
    own = own.strip()
    if opponent == "A": # opponent rock
        if own == "X":
            pointsCounter += 3 + 1 # draw + rock
        elif own == "Y":
            pointsCounter += 6 + 2 # win + paper
        elif own == "Z":
            pointsCounter += 0 + 3 # lost + scissor
        else:
            wtf = True
    elif opponent == "B": # opponent paper
        if own == "X":
            pointsCounter += 0 + 1 # lost + rock
        elif own == "Y":
            pointsCounter += 3 + 2 # win + paper
        elif own == "Z":
            pointsCounter += 6 + 3 # lost + scissor 
        else:
            wtf = True
    elif opponent == "C": # opponent scissor
        if own == "X":
            pointsCounter += 6 + 1 # lost + rock
        elif own == "Y":
            pointsCounter += 0 + 2 # win + paper
        elif own == "Z":
            pointsCounter += 3 + 3 # lost + scissor
        else:
            wtf = True
    else:
            wtf = True

print("wtf: " + str(wtf))
print("Points: " + str(pointsCounter))
