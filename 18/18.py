# DON'T COMPLAIN ABOUT ANYTHING, IT'S WORKING, OK!?

from __future__ import print_function
import matplotlib.pyplot as plt
import sys

map = []

tomove = sys.argv[2]

possibleKeys = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
possibleDoors = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'}
existingKeys = set()
existingDoors = set()

coords = {}

with open(sys.argv[1]) as f:
    for line in f:
        map.append([])
        for char in line.strip():
            map[len(map) - 1].append(char)
            if char in possibleKeys:
                existingKeys.add(char)
            elif char in possibleDoors:
                existingDoors.add(char)


for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] != '#' and map[i][j] != '.':
            coords[map[i][j]] = (j, i)


#Step 1 - Generate distances in labyrinth

class AStarGraph(object):
	#Define a class board like grid with two barriers

    def heuristic(self, start, goal):

        dx = abs(start[0] - goal[0])
        dy = abs(start[1] - goal[1])
        return dx + dy

    def get_vertex_neighbours(self, pos):
        n = []
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            x2 = pos[0] + dx
            y2 = pos[1] + dy

            s = map[y2][x2]

            if y2 < 0 or y2 > (len(map) - 1) or x2 < 0 or x2 > (len(map[y2]) - 1) or (s == '#'):
                continue

            n.append((x2, y2))
        return n

    def move_cost(self, a, b):
        return 1

def AStarSearch(start, end, map, graph):

    G = {} #Actual movement cost to each position from the start position
    F = {} #Estimated movement cost of start to end going via this position

	#Initialize starting values
    G[start] = 0
    F[start] = graph.heuristic(start, end)

    closedVertices = set()
    openVertices = set([start])
    cameFrom = {}

    while len(openVertices) > 0:
		#Get the vertex in the open list with the lowest F score
        current = None
        currentFscore = None
        for pos in openVertices:
            if current is None or F[pos] < currentFscore:
                currentFscore = F[pos]
                current = pos

        if current == end:
			#Retrace our route backward
            endPos = current
            path = [current]
            while current in cameFrom:
                current = cameFrom[current]
                path.append(current)
            path.reverse()
            return path, F[endPos] #Done!

		#Mark the current vertex as closed
        openVertices.remove(current)
        closedVertices.add(current)

		#Update scores for vertices near the current position
        for neighbour in graph.get_vertex_neighbours(current):
            if neighbour in closedVertices:
                continue #We have already processed this node exhaustively
            candidateG = G[current] + graph.move_cost(current, neighbour)

            if neighbour not in openVertices:
                openVertices.add(neighbour) #Discovered a new vertex
            elif candidateG >= G[neighbour]:
                continue #This G score is worse than previously found

			#Adopt this G score
            cameFrom[neighbour] = current
            G[neighbour] = candidateG
            H = graph.heuristic(neighbour, end)
            F[neighbour] = G[neighbour] + H

    #raise RuntimeError("A* failed to find a solution")
    return [], 0

existingObjects = existingKeys.union(existingDoors)
for i in tomove:
    existingObjects.add(i)

costs = {}

for k1 in existingObjects:
    for k2 in existingObjects:
        if k1 == k2:
            continue
        if (k2, k1) in costs:
            costs[(k1, k2)] = costs[(k2, k1)]
            continue
        start = coords[k1]
        end = coords[k2]
        graph = AStarGraph()
        result, cost = AStarSearch(start, end, map, graph)
        if len(result) > 0 and cost > 0:
            costs[(k1, k2)] = cost

#Step 2 - Generate dependency graph

def get_vertex_neighbours(pos):
    n = set()
    for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
        x2 = pos[0] + dx
        y2 = pos[1] + dy

        s = map[y2][x2]

        if y2 < 0 or y2 > (len(map) - 1) or x2 < 0 or x2 > (len(map[y2]) - 1) or (s == '#'):
            continue

        n.add((x2, y2))
    return n

def bfs(start):

    visited, queue = set(), [(coords[start], '')]
    res = set()
    while queue:
        vertex = queue.pop(0)
        if vertex[0] not in visited:
            o = map[vertex[0][1]][vertex[0][0]]
            if o != start and o in existingDoors:
                visited.add(vertex[0])
                for i in get_vertex_neighbours(vertex[0]) - visited:
                    no = (i, vertex[1] + o)
                    queue.append(no)
            elif o != start and o in existingObjects:
                res.add((o, vertex[1]))
            else:
                visited.add(vertex[0])
                for i in get_vertex_neighbours(vertex[0]) - visited:
                    no = (i, vertex[1])
                    queue.append(no)

    return res

possibilities = {}

for k in existingObjects:
    if k in existingDoors:
        continue
    possibilities[k] = bfs(k)

print(possibilities)

#Step 3 - Solve this shit!

class AStarGraph2(object):

    def __init__(self, costs):
        self.costs = costs
        self.possibleKeys = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
        self.possibleDoors = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'}

    def heuristic(self, start, goal):
        return 0

    def get_vertex_neighbours(self, pos):
        n = set()
        for i in pos[0]:
            for possibility in possibilities[i]:
                ok = True
                for door in possibility[1]:
                    if door.lower() not in pos[1]:
                        ok = False
                if ok:
                    if possibility[0] not in self.possibleKeys or possibility[0] in pos[1]:
                        n.add((pos[0].replace(i, possibility[0]), pos[1]))
                    else:
                        n.add((pos[0].replace(i, possibility[0]), "".join(sorted(pos[1] + possibility[0]))))
        return n

    def move_cost(self, a, b):
        for i in range(len(a[0])):
            if a[0][i] != b[0][i]:
                return costs[(a[0][i], b[0][i])]

def AStarSearch2(start, end, map, graph):

    G = {} #Actual movement cost to each position from the start position
    F = {} #Estimated movement cost of start to end going via this position

	#Initialize starting values
    G[start] = 0
    F[start] = graph.heuristic(start, end)

    closedVertices = set()
    openVertices = set([start])
    cameFrom = {}

    while len(openVertices) > 0:
		#Get the vertex in the open list with the lowest F score
        current = None
        currentFscore = None
        for pos in openVertices:
            if current is None or F[pos] < currentFscore:
                currentFscore = F[pos]
                current = pos

        if len(current[1]) == end:
			#Retrace our route backward
            endPos = current
            path = [current]
            while current in cameFrom:
                current = cameFrom[current]
                path.append(current)
            path.reverse()
            return path, F[endPos] #Done!

		#Mark the current vertex as closed
        openVertices.remove(current)
        closedVertices.add(current)

		#Update scores for vertices near the current position
        for neighbour in graph.get_vertex_neighbours(current):
            if neighbour in closedVertices:
                continue #We have already processed this node exhaustively
            candidateG = G[current] + graph.move_cost(current, neighbour)

            if neighbour not in openVertices:
                openVertices.add(neighbour) #Discovered a new vertex
            elif candidateG >= G[neighbour]:
                continue #This G score is worse than previously found

			#Adopt this G score
            cameFrom[neighbour] = current
            G[neighbour] = candidateG
            H = graph.heuristic(neighbour, end)
            F[neighbour] = G[neighbour] + H

    raise RuntimeError("A* failed to find a solution")

s = (tomove, '')
end = len(existingKeys)
graph = AStarGraph2(costs)
result, cost = AStarSearch2(s, end, map, graph)
print(result)
print(cost)
