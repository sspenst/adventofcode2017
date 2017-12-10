import sys

class Program:
	def __init__(self, line):
		self.num = int(line.split("(")[1].split(")")[0])

		# if there is no "->" then it is a leaf node
		if "->" not in line:
			self.name = line.split(" ")[0]
			self.pointers = None
			self.total = self.num
			self.leaf = True
		else:
			parts = line.split("->")
			self.name = parts[0].split(" ")[0]
			self.pointers = [word.strip() for word in parts[1].split(",")]
			self.total = 0
			self.leaf = False

programs = []

def get_program_from_name(name):
	for program in programs:
		if name == program.name:
			return program
	return None

def sum_sub_programs(name):
	cur_prog = get_program_from_name(name)

	# return immediately if the Program is a leaf node
	if cur_prog.leaf:
		return cur_prog.total
	else:
		total = cur_prog.num
		name_to_num_dict = {}
		num_dict = {}

		# loop through the sub programs to get the total
		# also keep track of child data in dictionaries
		for sub_name in cur_prog.pointers:
			cur_num = sum_sub_programs(sub_name)
			name_to_num_dict[sub_name] = cur_num
			if cur_num not in num_dict:
				num_dict[cur_num] = False 
			else:
				num_dict[cur_num] = True
			total += cur_num

		# check if there is a weight mismatch
		if len(num_dict) != 1:
			# find the incorrect and correct weights
			false_key = -1
			true_key = -1
			for key in num_dict:
				if num_dict[key] == False:
					false_key = key
				else:
					true_key = key

			# calculate what the incorrect weight should be so
			# that the disc would be balanced
			for prog_name, num in name_to_num_dict.items():
				if num == false_key:
					cur_num = get_program_from_name(prog_name).num
					print(cur_num - (false_key - true_key))
					sys.exit()
		return total

with open('input', 'r') as f:
	lines = f.read().strip().split("\n")
	for line in lines:
		programs.append(Program(line))

	# get the head Program
	cur_prog = programs[0]
	while 1:
		name_found = False
		for i in range(len(programs)):
			if programs[i].pointers != None and cur_prog.name in programs[i].pointers:
				cur_prog = programs[i]
				name_found = True
				break
		if name_found is False:
			break
	head_prog = cur_prog

	# recursively compute the sum of each Program
	sum_sub_programs(head_prog.name)
