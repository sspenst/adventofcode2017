def dance(p, moves):
    for move in moves:
        if move[0] == 's':
            spin = int(move[1:])
            a = p[spin*-1:]
            b = p[:len(p)-spin]
            p = a + b
        elif move[0] == 'x':
            a, b = list(map(int, move[1:].split("/")))
            p[a], p[b] = p[b], p[a]
        elif move[0] == 'p':
            a, b = move[1:].split("/")
            ai = p.index(a)
            bi = p.index(b)
            p[ai], p[bi] = p[bi], p[ai]
    return p

with open('input', 'r') as f:
    moves = f.read().strip().split(",")

    init = [chr(i) for i in range(97,113)]
    p = init[:]

    res = [''.join(init)]
    idx = 0

    while True:
        p = dance(p, moves)
        s = ''.join(p)
        if s not in res:
            res.append(s)
        else:
            idx = res.index(s)
            break

    cycle = len(res) - idx

    print(''.join(res[1000000000 % cycle]))
