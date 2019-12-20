import sys

maze = []

with open(sys.argv[1]) as f:
    for line in f:
        maze.append(line)

paths = {}
possiblePaths = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'}

openings = {}

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
                if a + b not in openings:
                    openings[a + b] = c
                else:
                    paths[c] = openings[a + b]
                    paths[openings[a + b]] = c

start = openings["AA"]
goal = openings["ZZ"]

def getneighbours(pos):
    d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    n = set()
    for i in d:
        new = (pos[0] + i[0], pos[1] + i[1])
        if maze[new[1]][new[0]] == '.':
            n.add(new)
    if pos in paths:
        n.add(paths[pos])
    return n


def bfs(start, end):
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
print(path)
print(len(path) - 1)
