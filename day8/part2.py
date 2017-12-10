def check_cond(x, cond, y):
	return {
		'<': lambda x, y: x < y,
		'>': lambda x, y: x > y,
		'==': lambda x, y: x == y,
		'!=': lambda x, y: x != y,
		'<=': lambda x, y: x <= y,
		'>=': lambda x, y: x >= y
	}[cond](x, y)

with open('input', 'r') as f:
	lines = f.read().strip().split("\n")
	regs = {}
	max = None

	for line in lines:
		inst = line.split(" ")
		rd = inst[0]
		op = inst[1]
		amt = int(inst[2])
		rc = inst[4]
		cond = inst[5]
		val = int(inst[6])

		if rc not in regs:
			regs[rc] = 0

		if check_cond(regs[rc], cond, val):
			if rd not in regs:
				regs[rd] = 0

			if op == 'inc':
				regs[rd] += amt
			elif op == 'dec':
				regs[rd] -= amt

			if max == None or regs[rd] > max:
				max = regs[rd]

	print(max)
