import intcode as ic

program = ic.programFromFile("input.txt")

dirs = ["up", "right", "down", "left"]
d = { "up": (0, -1), "right": (1, 0), "down": (0, 1), "left": (-1, 0)}
dir = 0

paint = {}

done = False
ip = 0
rb = 0
input = [1]

x = 0
y = 0
minX = 0
maxX = 0
minY = 0
maxY = 0

while not done:
    (done, output, program, ip, rb) = ic.evaluate(program, input, ip, rb)

    paint[(x, y)] = output[0]

    if output[1] == 1:
        dir += 1
    else:
        dir -= 1

    nd = dirs[dir % 4]

    if x < minX:
        minX = x
    if x > maxX:
        maxX = x
    if y < minY:
        minY = y
    if y > maxY:
        maxY = y

    x += d[nd][0]
    y += d[nd][1]

    if (x, y) in paint:
        input.append(paint[(x, y)])
    else:
        input.append(0)

print("Squares painted: " + str(len(paint)))

for i in range(minY, maxY + 1):
    for j in range(minX, maxX + 1):
        if (j, i) in paint and paint[(j, i)] == 1:
            print "O",
        else:
            print " ",
    print ""
