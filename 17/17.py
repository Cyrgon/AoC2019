import sys
import intcode as ic

program = ic.programFromFile("input.txt")
#program[0] = 2
input = []

map = []

(done, output, program, ip, rb) = ic.evaluate(program, input, 0, 0)

#94 -> UP
#118 -> DOWN
#62 -> RIGHT
#60 -> LEFT

row = 0
col = 0
map.append([])
for i in output:
    if i == 35:
        map[row].append('#')
    elif i == 46:
        map[row].append('.')
    elif i == 62:
        map[row].append('>')
    elif i == 94:
        map[row].append('^')
    elif i == 118:
        map[row].append('v')
    elif i == 60:
        map[row].append('<')
    elif i == 10:
        map.append([])
        row += 1
    else:
        print(i)

def isintersection(x, y):
    if x <= 0 or y <= 0 or (y >= len(map) - 1) or (x >= len(map[y]) - 1):
        return False

    if len(map[y + 1]) == 0:
        return False

    return map[y][x] == '#' and map[y - 1][x] == '#' and map[y + 1][x] == '#' and map[y][x - 1] == '#' and map[y][x + 1] == '#'

for i in range(len(map)):
    for j in range(len(map[i])):
        print map[i][j],
    print ""

s = 0

for i in range(len(map)):
    for j in range(len(map[i])):
        if isintersection(j, i):
            s += j * i

print(s)
