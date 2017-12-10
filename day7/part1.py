class Program:
	def __init__(self, line):
		if "->" not in line:
			self.name = line.split(" ")[0]
			self.pointers = None
		else:
			parts = line.split("->")
			self.name = parts[0].split(" ")[0]
			self.pointers = [word.strip() for word in parts[1].split(",")]

with open('input', 'r') as f:
	lines = f.read().strip().split("\n")
	programs = []
	for line in lines:
		programs.append(Program(line))
	
	cur_prog = programs[0]
	while 1:
		name_found = False
		for i in range(len(programs)):
			if programs[i].pointers != None and cur_prog.name in programs[i].pointers:
				cur_prog = programs[i]
				name_found = True
				break
		if name_found is False:
			print(cur_prog.name)
			break
