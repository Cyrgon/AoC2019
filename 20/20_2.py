import sys

maze = []

with open(sys.argv[1]) as f:
    for line in f:
        maze.append(line)

paths = {}
possiblePaths = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'}

openings = {}
names = {}

pathsIn = {}
pathsOut = {}

for i in range(len(maze)):
    for j in range(len(maze[i])):
        if maze[i][j] in possiblePaths:
            foundPath = False
            if i > 0 and maze[i - 1][j] == '.':
                a = maze[i][j]
                b = maze[i + 1][j]
                c = (j, i - 1)
                foundPath = True
            elif i < len(maze) - 1 and maze[i + 1][j] == '.':
                a = maze[i - 1][j]
                b = maze[i][j]
                c = (j, i + 1)
                foundPath = True
            elif j > 0 and maze[i][j - 1] == '.':
                a = maze[i][j]
                b = maze[i][j + 1]
                c = (j - 1, i)
                foundPath = True
            elif j < len(maze[i]) - 1 and maze[i][j + 1] == '.':
                a = maze[i][j - 1]
                b = maze[i][j]
                c = (j + 1, i)
                foundPath = True

            if foundPath:
                print(str(a) + " " + str(b) + " " + str(c))
                names[c] = a + b
                if a + b not in openings:
                    openings[a + b] = c
                else:
                    if c[0] < 3 or c[0] > len(maze[c[1]]) - 5 or c[1] < 3 or c[1] > len(maze) - 5:
                        pathsOut[c] = openings[a + b]
                        pathsIn[openings[a + b]] = c
                    else:
                        pathsIn[c] = openings[a + b]
                        pathsOut[openings[a + b]] = c

start = (openings["AA"], 0)
goal = (openings["ZZ"], 0)

print(start)
print(goal)

print("In: " + str(pathsIn) + "\n" + str(len(pathsIn)))
print("Out: " + str(pathsOut) + "\n" + str(len(pathsOut)))

def getneighbours(pos):
    coord = (pos[0][0], pos[0][1])
    d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    n = set()
    for i in d:
        new = ((coord[0] + i[0], coord[1] + i[1]), pos[1])
        if maze[new[0][1]][new[0][0]] == '.':
            n.add(new)
    if coord in pathsIn:
        n.add(((pathsIn[coord][0], pathsIn[coord][1]), pos[1] + 1))
    elif pos[1] > 0 and coord in pathsOut:
        n.add(((pathsOut[coord][0], pathsOut[coord][1]), pos[1] - 1))
    return n


def bfs(start, end):
    t = 0
    # maintain a queue of paths
    queue = []
    visited = set()
    # push the first path into the queue
    queue.append([start])
    while queue:
        # get the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]

        if node in visited:
            continue
        visited.add(node)

        # path found
        if node == end:
            return path
        # enumerate all adjacent nodes, construct a new path and push it into the queue
        for adjacent in getneighbours(node):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)

    print("No path found")
path = bfs(start, goal)

for p in path:
    if p[0] in names:
        print(names[p[0]] + " " + str(p[0]) + " " + str(p[1]))
print(len(path) - 1)
