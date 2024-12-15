grid, code = open('Input/Day15.txt').read().split('\n\n')

def move(position, direction):
    position += direction
    if all([grid[position] != '[' or move(position + 1, direction) and move(position, direction),
            grid[position] != ']' or move(position - 1, direction) and move(position, direction),
            grid[position] != 'O' or move(position, direction), grid[position] != '#']):
        grid[position], grid[position - direction] = grid[position - direction], grid[position]
        return True

for grid in grid, grid.translate(str.maketrans({'#': '##', '.':'..', 'O':'[]', '@':'@.'})):
    grid = {i+j*1j:c for j, r in enumerate(grid.split()) for i, c in enumerate(r)}

    position, = [p for p in grid if grid[p] == '@']

    for m in code.replace('\n', ''):
        dir = {'<':-1, '>':+1, '^':-1j, 'v':+1j}[m]
        C = grid.copy()
        if move(position, dir):
            position += dir
        else:
            grid = C
    result = sum(pos for pos in grid if grid[pos] in 'O[')
    print(int(result.real + result.imag*100))