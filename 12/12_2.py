import copy

# Problem input
positions = [
    {"x": -8, "y": -9, "z": -7},
    {"x": -5, "y": 2, "z": -1},
    {"x": 11, "y": 8, "z": -14},
    {"x": 1, "y": -4, "z": -11}
]

# # Example 1
# positions = [
#     {"x": -1, "y": 0, "z": 2},
#     {"x": 2, "y": -10, "z": -7},
#     {"x": 4, "y": -8, "z": 8},
#     {"x": 3, "y": 5, "z": -1}
# ]

# # Example 2
# positions = [
#     {"x": -8, "y": -10, "z": 0},
#     {"x": 5, "y": 5, "z": 10},
#     {"x": 2, "y": -7, "z": 3},
#     {"x": 9, "y": -8, "z": -3}
# ]

initial = copy.deepcopy(positions)

velocity = []
last = []
res = []
repeating = []
done = []
for i in range(0, len(positions)):
    velocity.append({})
    last.append({})
    res.append({})
    repeating.append({})
    done.append({})
    for key in positions[i]:
        velocity[i][key] = 0
        last[i][key] = 0
        res[i][key] = 0
        repeating[i][key] = []
        done[i][key] = False

numDone = 0
i = 0
while numDone < 12:
    if i > 0:
        for j in range(0, len(positions)):
            for key in positions[0].keys():
                if not done[j][key] and positions[j][key] == initial[j][key]:
                    repeating[j][key].append(i - last[j][key])
                    last[j][key] = i

                    listLen = len(repeating[j][key])
                    if listLen % 2 == 0:
                        if repeating[j][key][:listLen / 2] == repeating[j][key][listLen / 2:]:
                            done[j][key] = True
                            res[j][key] = sum(repeating[j][key][:listLen / 2])
                            numDone += 1

    # Gravity
    for j in range(0, len(positions)):
        for k in range(j + 1, len(positions)):
            for key in positions[j].keys():
                if positions[j][key] < positions[k][key]:
                    velocity[j][key] += 1
                    velocity[k][key] -= 1
                elif positions[j][key] > positions[k][key]:
                    velocity[j][key] -= 1
                    velocity[k][key] += 1

    # Velocity
    for j in range(0, len(positions)):
        for key in positions[j].keys():
            positions[j][key] += velocity[j][key]

    i += 1

# Part 2
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b / gcd(a, b)

tot = set()

for r in res:
    for k in r:
        tot.add(r[k])

l = 0
for val in tot:
    if l == 0:
        l = val
    else:
        l = lcm(l, val)
print("Repeating after " + str(l))
