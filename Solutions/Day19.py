towels, designs = open('Input/Day19.txt').read().split('\n\n')

towels = towels.split(', ')
designs = designs.splitlines()

def possible(design, t):
    if not design:
        return True
    
    for pattern in t:
        if design.startswith(pattern):
            if possible(design[(len(pattern)):], t):
                return True
    return False


good_towels = []

for pattern in towels:
    temp = [p for p in towels if p != pattern]
    if not possible(pattern, tuple(temp)):
        good_towels.append(pattern)


from functools import lru_cache
@lru_cache(None)
def count_ways(design ,t):
    if not design:
        return 1
    ways = 0
    for pattern in t:
        if design.startswith(pattern):
            ways += count_ways(design[len(pattern):], t)
    return ways

count = 0
for design in designs:
    if possible(design, good_towels):
        count += 1
print(count)

count = 0
for design in designs:
    count += count_ways(design, tuple(towels))
print(count)