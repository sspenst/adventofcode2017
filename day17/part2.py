with open('input', 'r') as f:
    steps = int(f.read().strip())

    buf = [0]

    cur = 0
    before_len = 0
    after_len = 0
    after_num = 0

    for i in range(1, 50000001):
        cur = ((cur + steps) % (before_len + 1 + after_len)) + 1

        if cur == (before_len + 1):
            after_num = i
            after_len += 1
        elif cur > (before_len + 1):
            after_len += 1
        elif cur < (before_len + 1):
            before_len += 1

    print(after_num)