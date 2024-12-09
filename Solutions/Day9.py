text = [int(x) for x in open('Input/Day9.txt').read()]

grid = [x // 2 if x % 2 == 0 else -1 for x, num in enumerate(text) for _ in range(num)]

while -1 in grid:
    if grid[-1] == -1:
        grid.pop()
    else:
        index = grid.index(-1)
        grid[index] = grid.pop()

print(sum(x * num for x, num in enumerate(grid)))

from collections import defaultdict
import heapq
grid = {}
holes = defaultdict(list)
position = 0

for x, num in enumerate(text):
    if x % 2 == 0:
        grid[x // 2] = [position, num]
    else:
        if num > 0:
            heapq.heappush(holes[num], position)
    position += num

for x in sorted(grid.keys(), reverse = True):
    start, length = grid[x]
    gaps = sorted([[holes[gap_length][0], gap_length] for gap_length in holes if gap_length >= length])
    if gaps:
        gap_start, gap_len = gaps[0]
        if start > gap_start:
            grid[x] = [gap_start, length]
            remaining = gap_len - length
            heapq.heappop(holes[gap_len])
            if not holes[gap_len]:
                del holes[gap_len]
            if remaining:
                heapq.heappush(holes[remaining], gap_start + length)
    
print(sum(num*(s*n+(n*(n-1))//2) for num, (s, n) in grid.items()))