from collections import Counter
text = open('Input/Day1.txt', 'r').read().splitlines()
left, right = [], []

for line in text:
    l, r = line.split('  ')
    left.append(int(l))
    right.append(int(r))

left = sorted(left)
right = sorted(right)
total = 0

for x in range(len(left)):
    total += abs(right[x] - left[x])

print(total)

count = Counter(right)

total = 0

for num in left:
    total += count[num] * num

print(total)