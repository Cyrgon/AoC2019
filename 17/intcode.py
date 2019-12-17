def read(program, pos):
    if pos not in program:
        program[pos] = 0
    return program[pos]

def store(value, program, pos):
    program[pos] = value

def getAction(action):
    return action % 100

def getParameterType(action, parNo):
    return (action // (pow(10, parNo + 2))) % 10

def getValue(program, ip, argNumber, rb):
    return read(program, getAddress(program, ip, argNumber, rb))

def getAddress(program, ip, argNumber, rb):
    parameterType = getParameterType(read(program, ip), argNumber)
    if parameterType == 0:
        return read(program, ip + argNumber + 1)
    elif parameterType == 1:
        return ip + argNumber + 1
    elif parameterType == 2:
        return rb + read(program, ip + argNumber + 1)
    else:
        raise Exception()

def evaluate(program, input, startIp, startRb):
    rb = startRb
    ip = startIp
    output = []

    while True:
        act = getAction(read(program, ip))

        def innerGetValue(argNo):
            return getValue(program, ip, argNo, rb)

        def innerGetAddress(argNo):
            return getAddress(program, ip, argNo, rb)

        if act == 99:
            return (True, output, None, None, None)
        if act == 1:
            store(innerGetValue(0) + innerGetValue(1), program, innerGetAddress(2))
            ip += 4
        elif act == 2:
            store(innerGetValue(0) * innerGetValue(1), program, innerGetAddress(2))
            ip += 4
        elif act == 3:
            if len(input) > 0:
                store(input.pop(0), program, innerGetAddress(0))
                ip += 2
            else:
                return (False, output, program, ip, rb)
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
                store(1, program, innerGetAddress(2))
            else:
                store(0, program, innerGetAddress(2))
            ip += 4
        elif act == 8:
            if innerGetValue(0) == innerGetValue(1):
                store(1, program, innerGetAddress(2))
            else:
                store(0, program, innerGetAddress(2))
            ip += 4
        elif act == 9:
            rb += innerGetValue(0)
            ip += 2
        else:
            raise Exception()

def programFromFile(file):
    with open(file) as f:
        return programFromString(f.readline())

def programFromString(string):
    list = string.strip().split(",")
    return dict([(x, int(list[x])) for x in range(0, len(list))])
