with open('input', 'r') as f:
    steps = int(f.read().strip())

    buf = [0]
    cur = 0
    after_num = 0

    for i in range(1, 50000001):
        cur = ((cur + steps) % i) + 1
        if cur == 1:
            after_num = i

    print(after_num)