with open('input', 'r') as f:
    moves = f.read().strip().split(",")

    p = [chr(i) for i in range(97,113)]
    size = len(p)

    for move in moves:
        if move[0] == 's':
            spin = int(move[1:])
            a = p[spin*-1:]
            b = p[:size-spin]
            p = a + b
        elif move[0] == 'x':
            a, b = list(map(int, move[1:].split("/")))
            p[a], p[b] = p[b], p[a]
        elif move[0] == 'p':
            a, b = move[1:].split("/")
            ai = p.index(a)
            bi = p.index(b)
            p[ai], p[bi] = p[bi], p[ai]

    print(''.join(p))