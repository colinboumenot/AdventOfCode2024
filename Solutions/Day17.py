registers, program = open('Input/Day17.txt').read().split('\n\n')
##registers, program = open('Solutions/test.txt').read().split('\n\n')
program = program.split(': ')[1].split(',')
print(program)
"""register_list = []
for line in registers.splitlines():
    register_list.append(int(line.split(': ')[1]))
index = 0
output = []

def combo_operand(operand):
    if operand == 4:
        return register_list[0]
    elif operand == 5:
        return register_list[1]
    elif operand == 6:
        return register_list[2]
    return operand

while index < len(program):
    opcode = int(program[index])
    operand = int(program[index + 1])

    if opcode == 0:
        denominator = 2 ** combo_operand(operand)
        register_list[0] //= denominator
    elif opcode == 1:
        register_list[1] ^= operand
    elif opcode == 2:
        register_list[1] = combo_operand(operand) % 8
    elif opcode == 3:
        if register_list[0] != 0:
            index = operand
            continue
    elif opcode == 4:
        register_list[1] ^= register_list[2]
    elif opcode == 5:
        output.append(combo_operand(operand) % 8)
    elif opcode == 6:
        denominator = 2 ** combo_operand(operand)
        register_list[1] = register_list[0] // denominator
    elif opcode == 7:
        denominator = 2 ** combo_operand(operand)
        register_list[2] = register_list[0] // denominator
    
    index += 2

print(','.join(map(str, output)))"""

def run(a, b, c):
    index = 0
    output = []
    while index in range(len(program)):
        C = {0:0, 1:1, 2:2, 3:3, 4:a, 5:b, 6:c}

        match program[index], program[index + 1]:
            case 0, opcode: a = a >> C[opcode]
            case 1, opcode: b = b ^ opcode
            case 2, opcode: b = 7 & C[opcode]
            case 3, opcode: index = opcode - 2 if a else index
            case 4, _: b = b ^ c
            case 5, opcode: output = output + [C[opcode] & 7]
            case 6, opcode: b = a >> C[opcode]
            case 7, opcode: c = a >> C[opcode]
        index += 2
    return output

    

program = [int(x) for x in program]
todo = [(1, 0)]
for i, a in todo:
    for a in range(a, a + 8):
        if run(a, 0, 0) == program[-i:]:
            todo += [(i+1, a * 8)]
            if i == len(program):
                print(a)
                break
