with open('input', 'r') as f:
    lines = f.read().strip().split("\n")

    size = len(lines[0])
    offset = size // 2

    weakened_nodes = []
    infected_nodes = []
    flagged_nodes = []

    nodes = {}

    for y in range(size):
        for x in range(size):
            if lines[y][x] == '#':
                nodes[(x-offset, y-offset)] = '#'
            else:
                nodes[(x-offset, y-offset)] = '.'

    posx = 0
    posy = 0

    # 0 - up
    # 1 - left
    # 2 - down
    # 3 - right
    dir = 0

    iterations = 10000000
    caused = 0
    a = 0
    b = 0
    c = 0

    for i in range(iterations):
        pos = (posx, posy)

        if pos not in nodes or nodes[pos] == '.':
            nodes[pos] = 'W'
            dir = (dir + 1) % 4
        elif nodes[pos] == 'W':
            nodes[pos] = '#'
            caused += 1
        elif nodes[pos] == '#':
            nodes[pos] = 'F'
            dir = (dir + 3) % 4
        else:
            nodes[pos] = '.'
            dir = (dir + 2) % 4

        if dir == 0:
            posy -= 1
        elif dir == 1:
            posx -= 1
        elif dir == 2:
            posy += 1
        else:
            posx += 1

    print(caused)
