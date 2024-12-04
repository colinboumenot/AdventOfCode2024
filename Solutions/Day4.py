text = open('Input/Day4.txt', 'r').read().splitlines()
length = len(text[0])
width = len(text)
target = 'XMAS'
target_len = len(target)
total = 0


directions = [
    (1, 0), (-1, 0),
    (0, 1), (0, -1),
    (1, 1), (-1, -1),
    (1, -1), (-1, 1)
]

def search(i, j, index, direction):
    if index == target_len:
        return 1
    ni, nj = i + direction[0], j + direction[1]
    if 0 <= ni < width and 0 <= nj < length and text[ni][nj] == target[index]:
        return search(ni, nj, index + 1, direction)
    return 0

for i in range(width):
    for j in range(length):
        if text[i][j] == 'X':
            for direction in directions:
                total += search(i, j, 1, direction)

print(total)

total = 0
def search_two(i, j):
    if (i + 1) in range(width) and (i - 1) in range(width) and (j + 1) in range(length) and (j - 1) in range(length):
        if set([text[i - 1][j - 1], text[i + 1][j + 1]]) == set([text[i + 1][j - 1], text[i - 1][j + 1]]) == set(['M', 'S']):
            return 1
        else:
            return 0
    else:
        return 0

    

for i in range(width):
    for j in range(length):
        if text[i][j] == 'A':
            total += search_two(i, j)

print(total)
            