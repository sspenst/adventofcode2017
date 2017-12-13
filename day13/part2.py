import sys

with open('input', 'r') as f:
    lines = f.read().strip().split("\n")
    tups = []
    for line in lines:
        tups.append(list(map(int, line.split(": "))))

    total = 0
    delay = 0

    while 1:
        total = 0
        caught = False
        for tup in tups:
            layer = tup[0]
            depth = tup[1]
            if (layer + delay) % ((depth - 1)*2) == 0:
                caught = True
                total += layer*depth

        if total == 0 and caught == False:
            print(delay)
            sys.exit()

        delay += 1