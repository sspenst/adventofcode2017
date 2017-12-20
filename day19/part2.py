with open('input', 'r') as f:
    lines = f.read().split("\n")

    width = len(lines[0])
    height = len(lines)

    x = 0
    y = 0

    # 0 - down
    # 1 - right
    # 2 - up
    # 3 - left
    direction = 0

    letters = ""

    for i in range(width):
        if lines[0][i] == '|':
            x = i
            break

    steps = 1

    while True:
        if direction == 0:
            y += 1
        elif direction == 1:
            x += 1
        elif direction == 2:
            y -= 1
        elif direction == 3:
            x -= 1

        c = lines[y][x]

        if c == '+':
            if lines[y-1][x] != ' ' and direction != 0:
                direction = 2
            elif lines[y][x+1] != ' ' and direction != 3:
                direction = 1
            elif lines[y+1][x] != ' ' and direction != 2:
                direction = 0
            elif lines[y][x-1] != ' ' and direction != 1:
                direction = 3
        elif c != '|' and c != '-' and c != ' ':
            letters += c
        elif c == ' ':
            break

        steps += 1

    print(steps)