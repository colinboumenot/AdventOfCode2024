text, operations = open('Input/Day24.txt').read().split('\n\n')

##text, operations = open('Solutions/test.txt').read().split('\n\n')
"""
from collections import defaultdict
gates = defaultdict(int)

for line in text.splitlines():
    loc, num = line.split(': ')
    gates[loc] = int(num)

ends = set()
for line in operations.splitlines():
    end = line.split(' -> ')[1]
    ends.add(end)

todo = [line for line in operations.splitlines()]
while todo:
    new_todo = []
    for line in todo:
        start, end = line.split(' -> ')
        if 'XOR' in start:
            gate1, gate2 = start.split(' XOR ')
            if (gate1 not in gates and gate1 in ends) or (gate2 not in gates and gate2 in ends):
                new_todo.append(line)
            else:
                gate1, gate2 = gates[gate1], gates[gate2]
                if gate1 != gate2:
                    gates[end] = 1
                else:
                    gates[end] = 0
        elif 'AND' in start:
            gate1, gate2 = start.split(' AND ')
            if (gate1 not in gates and gate1 in ends) or (gate2 not in gates and gate2 in ends):
                new_todo.append(line)
            else:
                gate1, gate2 = gates[gate1], gates[gate2]
                if gate1 and gate2:
                    gates[end] = 1
                else:
                    gates[end] = 0
        else:
            gate1, gate2 = start.split(' OR ')
            if (gate1 not in gates and gate1 in ends) or (gate2 not in gates and gate2 in ends):
                new_todo.append(line)
            else:
                gate1, gate2 = gates[gate1], gates[gate2]
                if gate1 or gate2:
                    gates[end] = 1
                else:
                    gates[end] = 0
    todo = new_todo

z = []
for x in range(10):
    z.insert(0, str(gates[f"z0{str(x)}"]))
for x in range(10, 46):
    z.insert(0, str(gates[f"z{str(x)}"]))

print(z)
z = ''.join(z)
print(int(z, 2))
"""

def process(op, op1, op2):
    if op == "AND":
        return op1 & op2
    elif op == "XOR":
        return op1 ^ op2
    else:
        return op1 | op2

wires = {}
for line in text.splitlines():
    wire, value = line.split(': ')
    wires[wire] = int(value)
ops = []
for line in operations.splitlines():
    op1, op, op2, _, result = line.split(' ')
    ops.append((op1, op, op2, result))

switched = set()

for op1, op, op2, result in ops:
    if result[0] == 'z' and op != 'XOR' and result != 'z45':
        switched.add(result)
    if (op == 'XOR' and result[0] not in ['x', 'y', 'z'] and op1[0] not in ['x', 'y', 'z'] and op2[0] not in ['x', 'y', 'z']):
        switched.add(result)
    if op == 'AND' and 'x00' not in [op1, op2]:
        for subop1, subop, subop2, subresult in ops:
            if (result == subop1 or result == subop2) and subop != 'OR':
                switched.add(result)
    if op == 'XOR':
        for subop1, subop, subop2, subresult in ops:
            if (result == subop1 or result == subop2) and subop == 'OR':
                switched.add(result)

print(','.join(sorted(switched)))


