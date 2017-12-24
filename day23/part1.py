import sys

def get_value(regs, reg):
    try:
        return int(reg)
    except ValueError:
        return regs[reg]

with open('input', 'r') as f:
    insts = f.read().strip().split("\n")

    mem = [inst.split(" ") for inst in insts]
    addr = 0
    regs = {}

    for c in range(ord('a'), ord('h') + 1):
        regs[chr(c)] = 0

    total = 0

    while True:
        try:
            i = mem[addr]
        except IndexError:
            print(total)
            sys.exit()

        if i[0] == 'set':
            regs[i[1]] = get_value(regs, i[2])
        elif i[0] == 'sub':
            regs[i[1]] -= get_value(regs, i[2])
        elif i[0] == 'mul':
            regs[i[1]] *= get_value(regs, i[2])
            total += 1
        elif i[0] == 'jnz':
            val = get_value(regs, i[1])
            if val != 0:
                addr += get_value(regs, i[2]) - 1

        addr += 1