import heapq
text = open('Input/Day16.txt').read().splitlines()
##text = open('Solutions/test.txt').read().splitlines()
grid = []
for line in text:
    row = []
    for item in line:
        row.append(item)
    grid.append(row)

for y, row in enumerate(grid):
    for x, item in enumerate(row):
        if item == 'S':
            start = (x, y)
        elif item == 'E':
            end = (x, y)

def heuristic(position, end):
    return abs(position[0] - end[0]) + abs(position[1] - end[1])

def is_valid(grid, x, y):
    return y in range(len(grid)) and x in range(len(grid[0])) and grid[y][x] != '#'

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
pq = [(0,0, start[0], start[1], 0)]
visited = set()
from collections import defaultdict
paths = defaultdict(set)
final_cost = None
while pq:
    _, cost, x, y, direction = heapq.heappop(pq)
    if (x, y) == end:
        print(cost)
        break
    if (x, y, direction) in visited:
        continue
    visited.add((x, y, direction))

    dx, dy = directions[direction]
    nx, ny = x + dx, y + dy
    if is_valid(grid, nx, ny):
        paths[(nx, ny)].add((x, y))
        heapq.heappush(pq, (cost + 1 + heuristic((nx, ny), end), cost + 1, nx, ny, direction))
    new_direction = (direction - 1) % 4
    heapq.heappush(pq, (cost + 1000 + heuristic((x, y), end), cost + 1000, x, y, new_direction))
    new_direction = (direction + 1) % 4
    heapq.heappush(pq, (cost + 1000 + heuristic((x, y), end), cost + 1000, x, y, new_direction))



import networkx

graph = networkx.DiGraph()

directions = (1, -1, 1j, -1j)

for i, row in enumerate(text):
    for j, cell in enumerate(row):
        if cell == '#':
            continue
        z = i + 1j * j
        if cell == 'S':
            start = (z, 1j)
        if cell == 'E':
            end = z
        for dz in directions:
            graph.add_node((z, dz))
for z, dz in graph.nodes:
    if (z + dz, dz) in graph.nodes:
        graph.add_edge((z, dz), (z + dz, dz), weight = 1)
    for move in -1j, 1j:
        graph.add_edge((z, dz), (z, dz * move), weight = 1000)

for dz in directions:
    graph.add_edge((end, dz), 'end', weight = 0)

print(len({z for path in networkx.all_shortest_paths(graph, start, 'end', weight = 'weight') for z, _ in path[:-1]}))
