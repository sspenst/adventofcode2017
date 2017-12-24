class Program:
    def __init__(self, pid):
        self.addr = 0
        self.regs = {}
        for c in range(ord('a'), ord('z') + 1):
            self.regs[chr(c)] = 0
        self.regs['p'] = pid
        self.pid = pid

    def exec(self):
        global mem
        global queue
        global sent
        global waiting
        i = mem[self.addr]

        if i[0] == 'set':
            try:
                self.regs[i[1]] = int(i[2])
            except ValueError:
                self.regs[i[1]] = self.regs[i[2]]
        elif i[0] == 'snd':
            if self.pid == 0:
                queue[1].append(self.regs[i[1]])
            else:
                queue[0].append(self.regs[i[1]])
                sent += 1
        elif i[0] == 'add':
            try:
                self.regs[i[1]] += int(i[2])
            except ValueError:
                self.regs[i[1]] += self.regs[i[2]]
        elif i[0] == 'mul':
            try:
                self.regs[i[1]] *= int(i[2])
            except ValueError:
                self.regs[i[1]] *= self.regs[i[2]]
        elif i[0] == 'mod':
            try:
                self.regs[i[1]] %= int(i[2])
            except ValueError:
                self.regs[i[1]] %= self.regs[i[2]]
        elif i[0] == 'rcv':
            if len(queue[self.pid]) == 0:
                self.addr -= 1
                waiting[self.pid] = 1
            else:
                self.regs[i[1]] = queue[self.pid][0]
                queue[self.pid].pop(0)
                waiting[self.pid] = 0
        elif i[0] == 'jgz':
            val = 0
            try:
                val = int(i[1])
            except ValueError:
                val = self.regs[i[1]]
            if (val > 0):
                try:
                    self.addr += int(i[2]) - 1
                except ValueError:
                    self.addr += self.regs[i[2]] - 1

        self.addr += 1

insts = open('input', 'r').read().strip().split("\n")

mem = [inst.split(" ") for inst in insts]
queue = {0:[], 1:[]}
waiting = {0:0, 1:0}
sent = 0

p0 = Program(0)
p1 = Program(1)

while True:
    p0.exec()
    p1.exec()
    if waiting[0] == 1 and waiting[1] == 1:
        break

print(sent)