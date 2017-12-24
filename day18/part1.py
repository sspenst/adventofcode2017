with open('input', 'r') as f:
    insts = f.read().strip().split("\n")

    mem = [inst.split(" ") for inst in insts]
    addr = 0
    regs = {}

    for c in range(ord('a'), ord('z') + 1):
        regs[chr(c)] = 0

    snd = 0

    while True:
        i = mem[addr]

        if i[0] == 'set':
            try:
                regs[i[1]] = int(i[2])
            except ValueError:
                regs[i[1]] = regs[i[2]]
        elif i[0] == 'snd':
            snd = regs[i[1]]
        elif i[0] == 'add':
            try:
                regs[i[1]] += int(i[2])
            except ValueError:
                regs[i[1]] += regs[i[2]]
        elif i[0] == 'mul':
            try:
                regs[i[1]] *= int(i[2])
            except ValueError:
                regs[i[1]] *= regs[i[2]]
        elif i[0] == 'mod':
            try:
                regs[i[1]] %= int(i[2])
            except ValueError:
                regs[i[1]] %= regs[i[2]]
        elif i[0] == 'rcv':
            val = regs[i[1]]
            if val != 0:
                print(snd)
                break
        elif i[0] == 'jgz':
            val = regs[i[1]]
            if (val > 0):
                addr += int(i[2]) - 1

        addr += 1