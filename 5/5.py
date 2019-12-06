import math

def doAction(ip, action, list, argStart, input):

    act = getAction(action)

    def innerGetValue(argNo):
        return getValue(list, argStart, action, argNo)

    if act == 1:
        list[list[argStart + 2]] = innerGetValue(0) + innerGetValue(1)
        return ip + 4
    elif act == 2:
        list[list[argStart + 2]] = innerGetValue(0) * innerGetValue(1)
        return ip + 4
    elif act == 3:
        list[list[argStart]] = input.pop(0)
        return ip + 2
    elif act == 4:
        print(innerGetValue(0))
        return ip + 2
    elif act == 5:
        if innerGetValue(0) != 0:
            return innerGetValue(1)
        else:
            return ip + 3
    elif act == 6:
        if innerGetValue(0) == 0:
            return innerGetValue(1)
        else:
            return ip + 3
    elif act == 7:
        if innerGetValue(0) < innerGetValue(1):
            list[list[argStart + 2]] = 1
        else:
            list[list[argStart + 2]] = 0
        return ip + 4
    elif act == 8:
        if innerGetValue(0) == innerGetValue(1):
            list[list[argStart + 2]] = 1
        else:
            list[list[argStart + 2]] = 0
        return ip + 4
    else:
        raise Exception()

def getValue(list, pos, action, argNumber):
    parameterType = getParameterType(action, argNumber)
    if parameterType == 0:
        return list[list[pos + argNumber]]
    elif parameterType == 1:
        return list[pos + argNumber]
    else:
        raise Exception()

def getAction(action):
    return action % 10

def getParameterType(action, parNo):
    return (action // (pow(10, parNo + 2))) % 10

def evaluate(program, input):
    position = 0

    while position < program.count and program[position] != 99:
        try:
            position = doAction(position, program[position], program, position + 1, input)
        except:
            print("Exception")
            return -1
    return program[0]

f = open("5_2.txt")
program = [int(x) for x in f.readline().split(",")]
input = [5]

progCopy = list(program)
inputCopy = list(input)

value = evaluate(progCopy, inputCopy)
