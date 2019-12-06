orbits = {}
with open('6.txt') as f:
   for line in f:
       l = [x.strip() for x in line.split(")")]
       orbits[l[1]] = l[0]

you = []
san = []

def createPath(key, s):
    if key not in s:
        return []
    else:
        list = createPath(s[key], s)
        list.insert(0, key)
        return list

def count(key, s):
    if key not in s:
        return 0
    else:
        return 1 + count(s[key], s)

#Part 1
sum = 0
for key in orbits:
    sum += count(key, orbits)
print("Part 1: " + str(sum))

#Part 2
you = createPath("YOU", orbits)[1:]
san = createPath("SAN", orbits)[1:]

min = 1000000000

for key in you:
    if key in san:
        res = you.index(key) + san.index(key)
        if res < min:
            min = res

print("Part2: " + str(min))
