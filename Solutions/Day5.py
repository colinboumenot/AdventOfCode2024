from collections import defaultdict

rules, text = open('Input/Day5.txt', 'r').read().split('\n\n')
rule_dict = defaultdict(set)

for rule in rules.splitlines():
    x, y = rule.split('|')
    rule_dict[y].add(x)

total = 0
incorrect = set()

for line in text.splitlines():
    line = line.strip().split(',')
    middle = int(line[len(line) // 2])
    for item in line:
        for rule in rule_dict[item]:
            if rule in line:
                if line.index(rule) > line.index(item):
                    middle = 0
                    incorrect.add(tuple(x for x in line))
    total += middle

print(total)
swaps  = 0

def check_line(line):
    for item in line:
        for rule in rule_dict[item]:
            if rule in line:
                i = line.index(rule)
                j = line.index(item)
                if i > j:
                    line[i], line[j] = line[j], line[i]
                    global swaps
                    swaps += 1
                    return False, tuple(x for x in line)
    return True, None

total = 0

while incorrect:
    new_incorrect = set()
    for line in incorrect:
        line = list(x for x in line)
        middle = int(line[len(line) // 2])
        valid, addition = check_line(line)
        if valid:
            total += middle
        else:
            new_incorrect.add(addition)
    incorrect = new_incorrect

print(total)
print(f"swaps {swaps}")