from collections import defaultdict
text = open('Input/Day11.txt').read().split(' ')

"""
stones = [int(x) for x in text]
cache = defaultdict(set)

for _ in range(25):
    new_stones = []
    for stone in stones:
        if stone in cache:
            for x in cache[stone]:
                new_stones.append(x)
        elif stone == 0:
            new_stones.append(1)
            cache[stone].add(1)
        elif len(str(stone)) % 2 == 0:
            stone = str(stone)
            left = stone[0:len(stone) // 2]
            right = stone[len(stone) // 2:]
            new_stones.append(int(left))
            new_stones.append(int(right))
            cache[stone].add(left)
            cache[stone].add(right)
        else:
            new_stones.append(stone * 2024)
            cache[stone].add(stone * 2024)
    stones = new_stones
print(len(stones))

"""

stones = {}
for x in text:
    stones[int(x)] = 1

def blink(stones):
    new_stones = defaultdict(int)
    for stone, count in stones.items():
        if stone == 0:
            new_stones[1] += count
        elif len(str(stone)) % 2 == 0:
            s = str(stone)
            left, right = s[:len(s) // 2], s[len(s) // 2:]
            new_stones[int(left)] += count
            new_stones[int(right)] += count
        else:
            new_stones[stone * 2024] += count
    return new_stones

for _ in range(75):
    stones = blink(stones)
print(sum(stones.values()))