import sys
import intcode as ic

program = ic.programFromFile("input.txt")
program[0] = 2
map = []

def checkbounds(x, y):
    return x >= 0 and y >= 0 and y < len(map) and x < len(map[y])

def calcpath(map):
    #UP = 0
    #RIGHT = 1
    #DOWN = 2
    #LEFT = 3
    dir = 0
    x = 60
    y = 24
    dxy = {0: {'x': 0, 'y': -1}, 1: {'x': 1, 'y': 0}, 2: {'x': 0, 'y': 1}, 3: {'x': -1, 'y': 0}}
    res = ""
    l = 0
    while True:
        if checkbounds(x + dxy[dir]['x'], y + dxy[dir]['y']) and map[y + dxy[dir]['y']][x + dxy[dir]['x']] == '#':
            l += 1
            y += dxy[dir]['y']
            x += dxy[dir]['x']
        elif checkbounds(x + dxy[(dir + 1) % 4]['x'], y + dxy[(dir + 1) % 4]['y']) and map[y + dxy[(dir + 1) % 4]['y']][x + dxy[(dir + 1) % 4]['x']] == '#':
            if l > 0:
                res += str(l) + ","
            l = 0
            res += 'R,'
            dir = (dir + 1) % 4
        elif checkbounds(x + dxy[(dir - 1) % 4]['x'], y + dxy[(dir - 1) % 4]['y']) and map[y + dxy[(dir - 1) % 4]['y']][x + dxy[(dir - 1) % 4]['x']] == '#':
            if l > 0:
                res += str(l) + ","
            l = 0
            res += 'L,'
            dir = (dir - 1) % 4
        else:
            res += str(l)
            break
    return res

def findparts(path):
    orgPath = path
    for i in range(len(path)):
        if path.count(path[:i]) < 3:
            if path[i - 2] == ",":
                a = path[:i - 2]
            else:
                a = path[:i - 1]
            path = path.replace(a + str(','), '')
            path = path.replace(a, '')
            for j in range(len(path)):
                if path.count(path[:j]) < 3:
                    if path[j - 2] == ",":
                        b = path[:j - 2]
                    else:
                        b = path[:j - 1]
                    path = path.replace(b + str(','), '')
                    path = path.replace(b, '')
                    for k in range(len(path)):
                        if path.count(path[:k]) < 3:
                            if path[k - 2] == ",":
                                c = path[:k - 2]
                            else:
                                c = path[:j - 1]
                            path = path.replace(c + str(','), '')
                            path = path.replace(c, '')
                            print("A: " + a)
                            print("B: " + b)
                            print("C: " + c)
                            return (orgPath.replace(a, "A").replace(b, "B").replace(c, "C"), a, b, c)

# mr = [ord('A'), ord(','), ord('B'), ord(','), ord('A'), ord(','), ord('A'), ord(','), ord('B'), ord(','), ord('C'), ord(','), ord('B'), ord(','), ord('C'), ord(','), ord('C'), ord(','), ord('B'), 10]
# A = [ord('L'), ord(','), ord('1'), ord('2'), ord(','), ord('R'), ord(','), ord('8'), ord(','), ord('L'), ord(','), ord('6'), ord(','), ord('R'), ord(','), ord('8'), ord(','), ord('L'), ord(','), ord('6'), 10]
# B = [ord('R'), ord(','), ord('8'), ord(','), ord('L'), ord(','), ord('1'), ord('2'), ord(','), ord('L'), ord(','), ord('1'), ord('2'), ord(','), ord('R'), ord(','), ord('8'), 10]
# C = [ord('L'), ord(','), ord('6'), ord(','), ord('R'), ord(','), ord('6'), ord(','), ord('L'), ord(','), ord('1'), ord('2'), 10]

inp = [[]]

done = False
ip = 0
rb = 0

hasPath = False

while not done:
    input = inp.pop(0)

    (done, output, program, ip, rb) = ic.evaluate(program, input, ip, rb)

    map = []

    if done:
        print(output[len(output) - 1])
        break

    row = 0
    map.append([])
    for i in output:
        if i == 10:
            map.append([])
            row += 1
        else:
            map[row].append(chr(i))

    print ""
    for i in range(len(map)):
        for j in range(len(map[i])):
            print map[i][j],
        print ""

    if not hasPath:
        path = calcpath(map)
        hasPath = True
        (mr, A, B, C) = findparts(path)
        mr = [ord(x) for x in mr]
        mr.append(10)
        A = [ord(x) for x in A]
        A.append(10)
        B = [ord(x) for x in B]
        B.append(10)
        C = [ord(x) for x in C]
        C.append(10)
        inp = [mr, A, B, C, [ord('n'), 10]]
