import re
text = open('Input/Day3.txt').read()

pattern = r"mul\((-?\d+),\s*(-?\d+)\)"
pairs = re.findall(pattern, text)
result = 0

for pair in pairs:
    result += (int(pair[0]) * int(pair[1]))

print(result)

filtered = text.split('do()')
enabled = []

for line in filtered:
    enabled.append(line.split("don't()")[0])

text = "".join(enabled)

pairs = re.findall(pattern, text)
result = 0

for pair in pairs:
    result += (int(pair[0]) * int(pair[1]))

print(result)