import heapq

text = open('Input/Day20.txt').read()
"""
##text = open('Solutions/test.txt').read()
grid = []

for y, line in enumerate(text.splitlines()):
    row = []
    for x, item in enumerate(line):
        if item == 'S':
            start = (y, x)
        if item == 'E':
            end = (y, x)
        row.append(item)
    grid.append(row)

def djikstra(map):

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    pq = []
    heapq.heappush(pq, (0, start[0], start[1]))
    distances = [[float('inf')] * len(grid[0]) for _ in range(len(map))]
    distances[start[0]][start[1]] = 0
    visited = set()

    while pq:
        distance, x, y = heapq.heappop(pq)

        if (x, y) in visited:
            continue
        visited.add((x, y))
        if (x, y) == end:
            return distance
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if nx in range(len(map)) and ny in range(len(map[0])) and (nx, ny) not in visited and map[nx][ny] != '#':
                new_distance = distance + 1
                if new_distance < distances[nx][ny]:
                    distances[nx][ny] = new_distance
                    heapq.heappush(pq, (new_distance, nx, ny))
    return -1

time = djikstra(grid)
result = 0
for x in range(len(grid)):
    for y in range(len(grid[0])):
        if grid[x][y] == '#':
            grid[x][y] = '.'
            new_time = djikstra(grid)
            if time - new_time >= 100:
                result += 1
            grid[x][y] = '#'
print(result)
"""
from itertools import combinations
grid = {i + j*1j: c for i, r in enumerate(text.splitlines()) for j, c in enumerate(r) if c != '#'}
start, = (p for p in grid if grid[p] == 'S')

distance = {start: 0}
todo = [start]

for position in todo:
    for new in position - 1, position + 1, position -1j, position + 1j:
        if new in grid and new not in distance:
            distance[new] = distance[position] + 1
            todo += [new]
result = 0

for (p, i), (q ,j) in combinations(distance.items(), 2):
    d = abs((p-q).real) + abs((p-q).imag)
    if d < 21 and j - i - d >= 100:
        print(result)
        result += 1
print(result)