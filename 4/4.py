import math

count = 0

for i in range(245318,765748):
    num = i
    lastNum = 99
    hasSame = False
    numSame = 1
    isCorrect = True
    while num > 0:
        last = num % 10
        if last == lastNum:
            numSame += 1
        elif numSame == 2:
            hasSame = True
        else:
            numSame = 1
        if last > lastNum:
            isCorrect = False
            break
        num = math.floor(num / 10)
        lastNum = last

    if numSame == 2:
        hasSame = True
    if hasSame and isCorrect:
        count += 1

print(count)
