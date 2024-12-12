text = open('Input/Day12.txt').read().splitlines()

grid = {}

for y, line in enumerate(text):
    for x, item in enumerate(line):
        grid[x + y * 1j] = item

def find_region(grid, start):
    region = set([start])
    key = grid[start]
    queue = [start]
    while queue:
        position = queue.pop()
        for d in [1, -1, 1j, -1j]:
            new_position = position + d
            if new_position in grid and new_position not in region and grid[new_position] == key:
                region.add(new_position)
                queue.append(new_position)
    return region

regions = []
found = set(grid.keys())

while len(found) > 0:
    start = found.pop()
    region = find_region(grid, start)
    found -= region
    regions.append((grid[start], region))

def perimeter(region):
    perimeter = 0
    for position in region[1]:
        for d in [1, -1, 1j, -1j]:
            new_position = position + d
            if new_position not in region[1]:
                perimeter += 1
    return perimeter

result = 0
for region in regions:
    result += len(region[1]) * perimeter(region)

print(result)

def sides(region):
    perimeters = set()
    for position in region[1]:
        for d in [1, -1, 1j, -1j]:
            new_position = position + d
            if new_position not in region[1]:
                perimeters.add((new_position, d))
    sides = 0
    while len(perimeters) > 0:
        position, d = perimeters.pop()
        sides += 1
        next = position + d * 1j
        while (next, d) in perimeters:
            perimeters.remove((next, d))
            next += d * 1j
        next = position + d * -1j
        while (next, d) in perimeters:
            perimeters.remove((next, d))
            next += d * -1j
    return sides

result = 0
for region in regions:
    result += len(region[1]) * sides(region)

print(result)