with open('input', 'r') as f:
    steps = int(f.read().strip())

    buf = [0]
    cur = 0

    for i in range(1, 2018):
        cur = ((cur + steps) % len(buf)) + 1
        buf.insert(cur, i)

    print(buf[buf.index(2017)+1])