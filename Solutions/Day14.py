text = open("Input/Day14.txt").read().splitlines()

one = two = three = four = 0

for line in text:
    position, velocity = line.split(' ')
    px, py = position.split('=')[1].split(',')
    vx, vy = velocity.split('=')[1].split(',')
    dx, dy = int(vx) * 100, int(vy) * 100
    nx = (int(px) + int(dx)) % 101
    ny = (int(py) + int(dy)) % 103
    if nx < 50:
        if ny < 51:
            one += 1
        elif ny > 51:
            four += 1
    elif nx > 50:
        if ny < 51:
            two += 1
        elif ny > 51:
            three += 1

print(one * two * three * four)


def treeness(cycles):
    one = two = three = four = 0

    for line in text:
        position, velocity = line.split(' ')
        px, py = position.split('=')[1].split(',')
        vx, vy = velocity.split('=')[1].split(',')
        dx, dy = int(vx) * cycles, int(vy) * cycles
        nx = (int(px) + int(dx)) % 101
        ny = (int(py) + int(dy)) % 103
        if nx < 50:
            if ny < 51:
                one += 1
            elif ny > 51:
                four += 1
        elif nx > 50:
            if ny < 51:
                two += 1
            elif ny > 51:
                three += 1

    return one * two * three * four

print(min(range(10000), key = treeness))