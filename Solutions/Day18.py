text, extra = open('Input/Day18.txt').read().split('\n\n')
##text = open('Solutions/test.txt').read()

grid = [['.' for _ in range(71)] for _ in range(71)]

for line in text.splitlines():
    x, y = line.split(',')
    x, y = int(x), int(y)
    grid[y][x] = '#'

start = (0, 0)
end = (70, 70)

import heapq
"""
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
pq = []
heapq.heappush(pq, (0, start[0], start[1]))
distances = [[float('inf')] * len(grid[0]) for _ in range(len(grid))]
distances[start[0]][start[1]] = 0
visited = set()

while pq:
    distance, x, y = heapq.heappop(pq)

    if (x, y) in visited:
        continue
    visited.add((x, y))
    if (x, y) == end:
        print(distance)
        break
    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if nx in range(len(grid)) and ny in range(len(grid[0])) and (nx, ny) not in visited and grid[nx][ny] != '#':
            new_distance = distance + 1
            if new_distance < distances[nx][ny]:
                distances[nx][ny] = new_distance
                heapq.heappush(pq, (new_distance, nx, ny))
"""


def djikstra(map):
    start = (0, 0)
    end = (70, 70)


    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    pq = []
    heapq.heappush(pq, (0, start[0], start[1]))
    distances = [[float('inf')] * len(grid[0]) for _ in range(len(grid))]
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

            if nx in range(len(grid)) and ny in range(len(grid[0])) and (nx, ny) not in visited and grid[nx][ny] != '#':
                new_distance = distance + 1
                if new_distance < distances[nx][ny]:
                    distances[nx][ny] = new_distance
                    heapq.heappush(pq, (new_distance, nx, ny))
    return -1


for line in extra.splitlines():
    x, y = line.split(',')
    x, y = int(x), int(y)
    grid[y][x] = '#'
    if djikstra(grid) == -1:
        print(line)
        break