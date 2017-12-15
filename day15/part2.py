with open('input', 'r') as f:
    lines = f.read().strip().split("\n")

    mod = 2147483647

    gena = 516
    genb = 190

    a = []
    b = []

    mask = (1 << 16) - 1

    total = 0

    while True:
        gena = (gena * 16807) % mod
        genb = (genb * 48271) % mod

        if gena % 4 == 0:
            a.append(gena)
            if (len(a) >= 5000000 and len(b) >= 5000000):
                break

        if genb % 8 == 0:
            b.append(genb)
            if (len(a) >= 5000000 and len(b) >= 5000000):
                break

    for i in range(5000000):
        if a[i] & mask == b[i] & mask:
            total += 1

    print(total)
