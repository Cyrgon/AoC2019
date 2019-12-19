import intcode as ic


orgProg = ic.programFromFile("input.txt")

searchSize = 1500

def checkSquare(x, y):
    return ic.evaluate(orgProg.copy(), [x, y], 0, 0)[1][0] == 1 and ic.evaluate(orgProg.copy(), [x + 99, y], 0, 0)[1][0] == 1 and ic.evaluate(orgProg.copy(), [x, y + 99], 0, 0)[1][0] == 1 and ic.evaluate(orgProg.copy(), [x + 99, y + 99], 0, 0)[1][0] == 1


for i in range(1000, 1500, 1):
    t = [0, searchSize]
    new = t
    found = False
    rowFound = False
    while True:
        #print(new)
        for q in new:
            output = ic.evaluate(orgProg.copy(), [q, i], 0, 0)[1]
            if output[0] == 1:
                found = True
                b = q
                break
        if found:
            break
        new = []
        for j in range(len(t) - 1):
            newNumber = (t[j] + t[j + 1]) // 2
            if newNumber not in t:
                new.append(newNumber)
        if len(new) == 0:
            b = -1
            break
        t = sorted(t + new)

    # Beam at b
    if b > 0:
        end = searchSize - 1
        for j in range(b, searchSize):
            output = ic.evaluate(orgProg.copy(), [j, i], 0, 0)[1]
            if output[0] == 0:
                end = j - 1
                break
        if end > 99:
            if checkSquare(end - 99, i):
                row = i
                rowFound = True
                break

    if rowFound:
        break

    print(i)

for i in range(0, 10000):
    if checkSquare(i, row):
        print("Found at " + str(i * 10000 + row))
        break
