import math
import itertools

def getValue(list, pos, action, argNumber):
    parameterType = getParameterType(action, argNumber)
    if parameterType == 0:
        return list[list[pos + argNumber]]
    elif parameterType == 1:
        return list[pos + argNumber]
    else:
        raise Exception()

def getAction(action):
    return action % 100

def getParameterType(action, parNo):
    return (action // (pow(10, parNo + 2))) % 10

def evaluate(program, input, startIp):
    ip = startIp
    output = []

    while True:

        if ip >= program.count:
            return output

        act = getAction(program[ip])

        def innerGetValue(argNo):
            return getValue(program, ip + 1, program[ip], argNo)

        if act == 99:
            return (True, output, None, None)
        if act == 1:
            program[program[ip + 3]] = innerGetValue(0) + innerGetValue(1)
            ip += 4
        elif act == 2:
            program[program[ip + 3]] = innerGetValue(0) * innerGetValue(1)
            ip += 4
        elif act == 3:
            if len(input) > 0:
                program[program[ip + 1]] = input.pop(0)
                ip += 2
            else:
                return (False, output, program, ip)
        elif act == 4:
            output.append(innerGetValue(0))
            ip += 2
        elif act == 5:
            if innerGetValue(0) != 0:
                ip = innerGetValue(1)
            else:
                ip += 3
        elif act == 6:
            if innerGetValue(0) == 0:
                ip = innerGetValue(1)
            else:
                ip += 3
        elif act == 7:
            if innerGetValue(0) < innerGetValue(1):
                program[program[ip + 3]] = 1
            else:
                program[program[ip + 3]] = 0
            ip += 4
        elif act == 8:
            if innerGetValue(0) == innerGetValue(1):
                program[program[ip + 3]] = 1
            else:
                program[program[ip + 3]] = 0
            ip += 4
        else:
            raise Exception()

f = open("7.txt")
orgProgram = [int(x) for x in f.readline().split(",")]

permutations = list(itertools.permutations(range(5,10)))
max = 0

def orgProg():
    return list(orgProgram)

for permutation in permutations:
    signal = 0
    pos = 0
    programs = {}
    ips = {}
    while True:
        if pos in programs:
            program = programs[pos]
            startIp = ips[pos]
            input = [signal]
        else:
            program = orgProg()
            startIp = 0
            input = [permutation[pos], signal]

        (done, output, progState, ip) = evaluate(program, input, startIp)
        signal = output[0]

        if not done:
            programs[pos] = progState
            ips[pos] = ip
        elif pos == 4:
            break

        pos = (pos + 1) % 5

    if signal > max:
        max = signal

print(max)
