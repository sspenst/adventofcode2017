pos = 0
state = 1
steps = 12173597
ones = {}

while steps != 0:
    if pos not in ones:
        ones[pos] = 0
    if state == 1:
        if ones[pos] == 0:
            ones[pos] = 1
            pos += 1
            state = 2
        else:
            ones[pos] = 0
            pos -= 1
            state = 3
    elif state == 2:
        if ones[pos] == 0:
            ones[pos] = 1
            pos -= 1
            state = 1
        else:
            ones[pos] = 1
            pos += 1
            state = 4
    elif state == 3:
        if ones[pos] == 0:
            ones[pos] = 1
            pos += 1
            state = 1
        else:
            ones[pos] = 0
            pos -= 1
            state = 5
    elif state == 4:
        if ones[pos] == 0:
            ones[pos] = 1
            pos += 1
            state = 1
        else:
            ones[pos] = 0
            pos += 1
            state = 2
    elif state == 5:
        if ones[pos] == 0:
            ones[pos] = 1
            pos -= 1
            state = 6
        else:
            ones[pos] = 1
            pos -= 1
            state = 3
    elif state == 6:
        if ones[pos] == 0:
            ones[pos] = 1
            pos += 1
            state = 4
        else:
            ones[pos] = 1
            pos += 1
            state = 1
    steps -= 1

total = 0
for p in ones:
    if ones[p] == 1:
        total += 1
print(total)
