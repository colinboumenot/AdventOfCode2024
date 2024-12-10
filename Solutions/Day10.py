text = open('Input/Day10.txt').read().splitlines()
##text = open('Solutions/test.txt').read().splitlines()
grid = []
for line in text:
    grid_line = []
    for x in range(len(line)):
        grid_line.append(int(line[x]))
    grid.append(grid_line)

def search(i, j, current, visited):
    if i not in range(len(grid)) or j not in range(len(grid[0])) or (i, j) in visited:
        return 0
    if grid[i][j] == current + 1:
        visited.add((i, j))
        if grid[i][j] == 9:
            return 1
        else:
            return search(i + 1, j, current + 1, visited) + search(i - 1, j, current + 1, visited) + search(i, j + 1, current + 1, visited) + search(i, j - 1, current + 1, visited)
    else:
        return 0

total = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 0:
            total += search(i, j, -1, set())
print(total)

text = open('Input/Day10.txt').read().splitlines()
##text = open('Solutions/test.txt').read().splitlines()
grid = []
for line in text:
    grid_line = []
    for x in range(len(line)):
        grid_line.append(int(line[x]))
    grid.append(grid_line)

def search(i, j, current):
    if i not in range(len(grid)) or j not in range(len(grid[0])):
        return 0
    if grid[i][j] == current + 1:
        if grid[i][j] == 9:
            return 1
        else:
            return search(i + 1, j, current + 1) + search(i - 1, j, current + 1) + search(i, j + 1, current + 1) + search(i, j - 1, current + 1)
    else:
        return 0

total = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 0:
            total += search(i, j, -1)
print(total)