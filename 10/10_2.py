import numpy as np
import math

def angle(v1, v2):
    ac = angle_between(v1, v2)
    if v2[0] > 0:
        return 2 * math.pi - ac
    else:
        return ac

def unit_vector(vector):
    return vector / np.linalg.norm(vector)

def angle_between(v1, v2):
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))


def distance(p1, p2):
    a = p1[0] - p2[0]
    b = p1[1] - p2[1]
    return (math.sqrt(a * a + b * b))

start = (17.0, 22.0)
angles = {}
angleList = []

def add(astroid):
    if start == astroid:
        return

    dx = start[0] - astroid[0]
    dy = start[1] - astroid[1]

    ang = round(angle((0, 1), (dx, dy)), 5)

    if ang not in angles:
        angles[ang] = []
    if ang not in angleList:
        angleList.append(ang)
    angles[ang].append(astroid)

with open("input.txt") as f:
    y = 0.0
    for line in f:
        x = 0.0
        for i in line.strip():
            if i == "#":
                add((x, y))
            x += 1
        y += 1

angleList.sort()

count = 0
i = 0
while True:
    cDist = 1000000

    ang = angleList[i]
    for j in angles[ang]:
        dist = distance(start, j)
        if dist < cDist:
            cDist = dist
            closest = j
    angles[ang].remove(closest)
    if len(angles[ang]) == 0:
        angleList.remove(ang)
        if len(angleList) == 0:
            break
    else:
        i += 1

    i = i % len(angleList)
    count += 1
    if count == 200:
        print("Count: " + str(count) + ", remove: " + str(closest) + ", code: " + str(closest[0] * 100 + closest[1]))
        break
