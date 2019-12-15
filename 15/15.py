import sys
import intcode as ic
import random

program = ic.programFromFile(sys.argv[1])

uncharted = "."
wall = u"\u2588"
empty = " "
goal = "S"

gameBoard = []
for y in range(0, 40):
    gameBoard.append([])
    for x in range(0, 40):
        gameBoard[y].append(uncharted)

pos = (15, 5)
gameBoard[15][5] = empty
dir = 1
done = False

curSteps = 0
curStepsFromOxygen = 0
maxStepsFromOxygen = 0

minSteps = {
    pos: 0
}

minStepsFromOxygen = {}

hasFoundOxygen = False

def updateTile(fromPos, direction, response):
    global gameBoard

    if direction == 1:
        newPos = (fromPos[0], fromPos[1] - 1)
    elif direction == 2:
        newPos = (fromPos[0], fromPos[1] + 1)
    elif direction == 3:
        newPos = (fromPos[0] - 1, fromPos[1])
    elif direction == 4:
        newPos = (fromPos[0] + 1, fromPos[1])

    if response == 0:
        gameBoard[newPos[1]][newPos[0]] = wall
        return pos
    elif response == 1:
        gameBoard[newPos[1]][newPos[0]] = empty
        return newPos
    elif response == 2:
        gameBoard[newPos[1]][newPos[0]] = goal
        return newPos


ip = 0
rb = 0
while not done:
    (done, output, program, ip, rb) = ic.evaluate(program, [dir], ip, rb)

    pos = updateTile(pos, dir, output[0])

    curSteps += 1
    if pos in minSteps:
        if minSteps[pos] < curSteps:
            curSteps = minSteps[pos]

    minSteps[pos] = curSteps

    if hasFoundOxygen:
        curStepsFromOxygen += 1

        if pos in minStepsFromOxygen:
            if minStepsFromOxygen[pos] < curStepsFromOxygen:
                curStepsFromOxygen = minStepsFromOxygen[pos]

        minStepsFromOxygen[pos] = curStepsFromOxygen
        if curStepsFromOxygen > maxStepsFromOxygen:
            maxStepsFromOxygen = curStepsFromOxygen
            print("New oxygen max: " + str(maxStepsFromOxygen))

    if not hasFoundOxygen and output[0] == 2:
        print("Steps to goal: " + str(curSteps))
        hasFoundOxygen = True
        minStepsFromOxygen[pos] = 0
        curStepsFromOxygen = 0

        # Reset the board to uncharted to make the second search faster
        for y in range(0, len(gameBoard) - 1):
            for x in range(0, len(gameBoard) - 1):
                if gameBoard[y][x] == empty:
                    gameBoard[y][x] = uncharted

    if gameBoard[pos[1] - 1][pos[0]] == uncharted:
        dir = 1
    elif gameBoard[pos[1] + 1][pos[0]] == uncharted:
        dir = 2
    elif gameBoard[pos[1]][pos[0] + 1] == uncharted:
        dir = 4
    elif gameBoard[pos[1]][pos[0] - 1] == uncharted:
        dir = 3
    else:
        dir = random.randint(1,4)

    # for y in range(0, len(gameBoard)):
    #     for x in range(0, len(gameBoard[0])):
    #         if (x, y) == pos:
    #             print "V",
    #         elif (x, y) == (15, 5):
    #             print "O",
    #         else:
    #             print gameBoard[y][x],
    #     print ""
    # print ""
