from copy import deepcopy
text = [] 
for line in open('Input/Day6.txt', 'r').read().splitlines():
    text.append([x for x in line])

x, y = 0, 0
for i in range(len(text[0])):
    for j in range(len(text)):
        if text[i][j] == '^':
            x, y = i, j
            break

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
direction = 0
seen = 0
to_check = set()
while x in range(len(text[0])) and y in range(len(text)):
    text[x][y] = 'X'
    to_check.add((x, y))
    seen += 1
    move = directions[direction]
    dx, dy = move
    if text[x + dx][y + dy] == '#':
        if direction == 3:
            direction = 0
        else:
            direction += 1
        move = directions[direction]
        dx, dy = move
    x = x + dx
    y = y + dy

total = 0
for line in text:
    for item in line:
        if item == 'X':
            total += 1

print(total)

text = [] 
for line in open('Input/Day6.txt', 'r').read().splitlines():
    text.append([x for x in line])

x, y = 0, 0
for i in range(len(text[0])):
    for j in range(len(text)):
        if text[i][j] == '^':
            x, y = i, j
            break

def check_cycle(grid, f, g):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    direction = 0
    visited = set()
    while f in range(len(grid)) and g in range(len(grid[0])):
        grid[f][g] = 'X'
        if (f, g, direction) in visited:
            return True
        visited.add((f, g, direction))
        move = directions[direction]
        dx, dy = move
        if f + dx in range(len(grid)) and g + dy in range(len(grid[0])) and grid[f + dx][g + dy] == '#':
            direction = (direction + 1) % 4
        else:
            f = f + dx
            g = g + dy
    return False

result = 0

for f, g in to_check:
    if (f, g) != (x, y) and text[f][g] != '#':
        new_text = deepcopy(text)
        new_text[f][g] = '#'
        if check_cycle(new_text, x, y):
            result += 1

print(result)