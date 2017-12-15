with open('input', 'r') as f:
    lines = f.read().strip().split("\n")

    mod = 2147483647

    gena = 516
    genb = 190

    mask = (1 << 16) - 1

    total = 0

    for i in range(40000000):
        if i % 1000000 == 0:
            print(i)
        gena = (gena * 16807) % mod
        genb = (genb * 48271) % mod

        if gena & mask == genb & mask:
            total += 1

    print(total)
