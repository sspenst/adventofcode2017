with open('input', 'r') as f:
    dirs = f.read().strip().split(",")
    x = 0
    y = 0

    for dir in dirs:
        if dir == 'ne':
            x += 1
            y += 1
        elif dir == 'se':
            x += 1
            y -= 1
        elif dir == 's':
            y -= 2
        elif dir == 'n':
            y += 2
        elif dir == 'nw':
            x -= 1
            y += 1
        elif dir == 'sw':
            x -= 1
            y -= 1

    a = 0
    b = 0
    steps = 0

    while 1:
        if a < x and b <= y:
            a += 1
            b += 1
        elif a < x and b > y:
            a += 1
            b -= 1
        elif a > x and b <= y:
            a -= 1
            b += 1
        elif a > x and b > y:
            a -= 1
            b -= 1
        elif a == x and b > y:
            b -= 2
        elif a == x and b < y:
            b += 2
        else:
            print(steps)
            break
        steps += 1