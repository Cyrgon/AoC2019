import sys

reactions = {}

with open(sys.argv[1]) as f:
    for line in f:
        split = line.strip().split(" => ")
        res = split[1].split(" ")
        ingList = []
        for ing in split[0].split(", "):
            r = ing.split(" ")
            ingList.append((r[1], int(r[0])))
        reactions[res[1]] = (int(res[0]), ingList)

store = {}

def todo(material, amount):
    global store
    if material == "FUEL":
        store = {}
    amountNeededAfterLoad = amount
    if material in store:
        if store[material] >= amount:
            store[material] -= amount
            return (0, 0)
        else:
            amountNeededAfterLoad -= store[material]
            store[material] = 0
    ing = reactions[material][1]
    timesToRun = amountNeededAfterLoad // reactions[material][0]
    if amountNeededAfterLoad % reactions[material][0] > 0:
        timesToRun += 1

    extra = (reactions[material][0] * timesToRun) - amountNeededAfterLoad
    ore = 0
    for i in ing:
        if i[0] == "ORE":
            ore += i[1] * timesToRun
        else:
            prod = todo(i[0], i[1] * timesToRun)
            ore += prod[0]
            if i[0] not in store:
                store[i[0]] = 0
            store[i[0]] += prod[1]
    return (ore, extra)

print("1 FUEL needs " + str(todo("FUEL", 1)[0]) + " ORE")

goal = 1000000000000
min = 0
max = 10000000
while max - min > 1:
    middle = (max + min) // 2
    res = todo("FUEL", middle)
    if res[0] > goal:
        max = middle
    elif res[0] < goal:
        min = middle
    else:
        min = middle
        break

print(str(min) + " amount of FUEL can be produced by " + str(todo("FUEL", min)[0]) + " ORE")
