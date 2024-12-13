import re
from math import gcd
from itertools import product
text = open("Input/Day13.txt").read().split('\n\n')
##text = open("Solutions/test.txt").read().split('\n\n')


def solve_equation(ax, ay, bx, by, px, py):
    px = px + 10000000000000
    py = py + 10000000000000
    i = (bx * py - by * px) / (ay * bx - ax * by)
    j = (px - i * ax) / bx
    if (px - i * ax) % bx == 0 and (bx * py - by * px) % (ay * bx - ax * by) == 0:
        return 3 * int(i) + int(j)
    else:
        return 0
        

result = 0

for game in text:
    inputs = []
    for line in game.splitlines():
        x_data, y_data = line.split(': ')[1].split(', ')
        x, y = re.split(r'[+=]+', x_data)[1], re.split(r'[+=]+', y_data)[1]
        inputs.append(int(x))
        inputs.append(int(y))
    result += solve_equation(*inputs)
print(result)
