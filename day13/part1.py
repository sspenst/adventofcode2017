with open('input', 'r') as f:
    lines = f.read().strip().split("\n")

    total = 0

    for line in lines:
        layer, depth = list(map(int, line.split(": ")))
        if layer % ((depth - 1)*2) == 0:
            total += layer*depth

    print(total)