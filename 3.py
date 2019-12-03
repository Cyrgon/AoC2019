import sys
import csv
import math

fileName = "3_3.txt"

if len(sys.argv) > 1:
    fileName = sys.argv[1]

input = []

with open(fileName) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        input.append([])
        for item in row:
            input[line_count].append(item)
        line_count += 1

def parseAction(action):
    return (action[0], int(action[1:]))

def getStringPos(x, y):
    return str(x) + "," + str(y)

minManhattan = 100000000000
minSteps = 100000000000
positions = {}

first = True

for wire in input:

    posx = 0
    posy = 0
    steps = 0

    for action in wire:
        (direction, num) = parseAction(action)

        for i in range(num):
            if direction == 'R':
                posx += 1
            elif direction == 'L':
                posx -= 1
            elif direction == 'U':
                posy += 1
            elif direction == 'D':
                posy -= 1

            steps += 1

            strPos = getStringPos(posx, posy)

            if first:
                positions[strPos] = steps
            else:
                if strPos in positions:
                    totSteps = positions[strPos] + steps
                    manhattan = abs(posx) + abs(posy)
                    if totSteps < minSteps:
                        minSteps = totSteps
                    if manhattan < minManhattan:
                        minManhattan = manhattan

    first = False

print("Manhattan: " + str(minManhattan))
print("Steps: " + str(minSteps))
