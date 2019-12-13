import sys
import intcode as ic

program = ic.programFromFile("input.txt")

gameBoard = []
for y in range(0, 20):
    gameBoard.append([])
    for x in range(0, 44):
        gameBoard[y].append(0)

dir = 0
bdx = 1
ballPos = (20,15)
done = False

while not done:
    ip = 0
    rb = 0
    (done, output, program, ip, rb) = ic.evaluate(program, [dir], ip, rb)

    i = 0
    score = 0

    maxX = 0
    maxY = 0

    while i < len(output):
        x = output[i]
        y = output[i + 1]

        if x == -1 and y == 0:
            score = output[i + 2]
            i += 3
            continue

        if x > maxX:
            maxX = x
        if y > maxY:
            maxY = y

        tile = output[i + 2]

        if tile == 4:
            if x > ballPos[0]:
                bdx = 1
            else:
                bdx = -1
            ballPos = (x, y)
        elif tile == 3:
            padPos = (x, y)

        gameBoard[y][x] = tile

        i += 3

    print(score)

    if padPos[0] < ballPos[0] + bdx:
        dir = 1
    elif padPos[0] > ballPos[0]:
        dir = -1
    else:
        dir = 0

    for y in range(0, 20):
        for x in range(0, 44):
            if gameBoard[y][x] == 0:
                print " ",
            else:
                print gameBoard[y][x],
        print ""
    print ""
