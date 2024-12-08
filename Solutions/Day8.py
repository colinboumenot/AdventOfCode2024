import itertools
text = open('Input/Day8.txt').read()

grid = [list(line) for line in text.splitlines()]
frequencies = set()

for line in grid:
    for item in line:
        if item != '.':
            frequencies.add(item)

coordinates = [{(i, j) for i, line in enumerate(grid) for j, char in enumerate(line) if char == frequency} for frequency in frequencies]

def get_nodes(point):
    return {(2*x1-x2, 2*y1-y2) for (x1, y1), (x2, y2) in itertools.permutations(point, 2)}

nodes = set()
for coordinate in coordinates:
    nodes |= get_nodes(coordinate)

valid = {(i, j) for i, j in nodes if i in range(len(grid)) and j in range(len(grid[0]))}
print(len(valid))

def get_nodes(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    dx, dy = x2 - x1, y2 - y1
    nodes = set()
    nx, ny = x1, y1
    while nx in range(len(grid)) and ny in range(len(grid[0])):
        nodes.add((nx, ny))
        nx, ny = nx + dx, ny + dy
    nx, ny = x1, y1
    while nx in range(len(grid)) and ny in range(len(grid[0])):
        nodes.add((nx, ny))
        nx, ny = nx - dx, ny - dy
    return nodes

nodes = set()
for point in coordinates:
    for point1, point2 in itertools.combinations(point, 2):
        nodes |= get_nodes(point1, point2)
print(len(nodes))