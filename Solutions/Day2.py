text = open('Input/Day2.txt').read().splitlines()
safe = 0
recheck = []

def is_safe(vals):
    positive = set([1, 2, 3])
    negative = set([-1, -2, -3])
    for x in range(1, len(vals)):
        positive.add(vals[x] - vals[x - 1])
        negative.add(vals[x] - vals[x - 1])
    
    if len(positive) == 3 or len(negative) == 3:
        return True
    else:
        return False
    
for line in text:
    nums = [int(x) for x in line.split()]
    if is_safe(nums):
        safe += 1
    else:
        recheck.append(line)

print(safe)

for line in recheck:
    nums = [int(x) for x in line.split()]
    for x in range(len(nums)):
        if is_safe((nums[:x] + nums[x + 1:])):
            safe += 1
            break

print(safe)


