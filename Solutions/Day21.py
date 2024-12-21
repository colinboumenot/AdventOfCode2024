from collections import Counter
text = open('Input/Day21.txt').read().splitlines()
##text = open('Solutions/test.txt').read().splitlines()

key_pad = {c: (i % 3, i // 3) for i, c in enumerate('789456123 0A')}
dir_pad = {c: (i % 3, i // 3) for i, c in enumerate(' ^A<v>')}

def steps(grid, s, i = 1):
    px, py = grid['A']
    bx, by = grid[" "]
    result = Counter()
    for c in s:
        npx, npy = grid[c]
        f = npx == bx and py == by or npy == by and px == bx
        result[(npx - px, npy - py, f)] += i
        px, py = npx, npy
    return result

def step(n):
    output = 0
    for line in text:
        result = steps(key_pad, line)
        for _ in range(n +1):
            result = sum((steps(dir_pad, ('<' * -x + 'v' * y + '^' * -y + '>' * x)[:: -1 if f else 1] + 'A', result[(x, y, f)]) for x, y, f in result), Counter())
        output += result.total() * int(line[:3])
    return output

print(step(2))
print(step(25))
