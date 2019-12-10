def isbetween(s, mid, e):
    if s[0] == e[0]:
        return s[0] == mid[0] and (min(s[1], e[1]) <= mid[1]) and (mid[1] <= max(s[1], e[1]))
    if s[1] == e[1]:
        return s[1] == mid[1] and (min(s[0], e[0]) <= mid[0]) and (mid[0] <= max(s[0], e[0]))

    k = (s[1] - e[1]) / (s[0] - e[0])
    m = s[1] - k * s[0]

    return (mid[1] >= (k * mid[0] + m) * 0.999) and (mid[1] <= (k * mid[0] + m) * 1.001) and (min(s[0], e[0]) <= mid[0]) and (mid[0] <= max(s[0], e[0]))

map = set()

with open("input.txt") as f:
    y = 0.0
    for line in f:
        x = 0.0
        for i in line.strip():
            if i == "#":
                map.add((x, y))
            x += 1
        y += 1

maxC = 0

for start in map:
    count = 0
    for end in map:
        block = False
        if start == end:
            continue
        for middle in map:

            if middle == start or middle == end or start == end:
                continue

            if isbetween(start, middle, end):
                block = True
                break

        if not block:
            count += 1

    if count > maxC:
        maxC = count
        best = start
print("Max: " + str(maxC))
print("Best: " + str(best))
