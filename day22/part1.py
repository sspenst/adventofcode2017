def rotate(dir, infected):
    if dir == 'up':
        if infected:
            return 'right'
        else:
            return 'left'
    elif dir == 'left':
        if infected:
            return 'up'
        else:
            return 'down'
    elif dir == 'down':
        if infected:
            return 'left'
        else:
            return 'right'
    else:
        if infected:
            return 'down'
        else:
            return 'up'

with open('input', 'r') as f:
    lines = f.read().strip().split("\n")

    size = len(lines[0])
    offset = size // 2

    infected_nodes = []

    for y in range(size):
        for x in range(size):
            if lines[y][x] == '#':
                infected_nodes.append((x-offset, y-offset))

    posx = 0
    posy = 0
    dir = 'up'

    iterations = 10000
    caused = 0

    for i in range(iterations):
        infected = (posx, posy) in infected_nodes
        dir = rotate(dir, infected)

        if infected:
            infected_nodes.remove((posx, posy))
        else:
            infected_nodes.append((posx, posy))
            caused += 1

        if dir == 'up':
            posy -= 1
        elif dir == 'left':
            posx -= 1
        elif dir == 'down':
            posy += 1
        else:
            posx += 1

    print(caused)
