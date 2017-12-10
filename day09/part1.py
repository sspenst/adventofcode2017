with open('input', 'r') as f:
	stream = f.read().strip()
	score = 0
	depth = 0
	garbage = False
	skip = False

	for c in stream:
		if skip:
			skip = False
		elif garbage and c == '!':
			skip = True
		elif garbage and c == '>':
			garbage = False
		elif garbage:
			continue
		elif c == '<':
			garbage = True
		elif c == '{':
			depth += 1
			score += depth
		elif c == '}':
			depth -= 1
		elif c == ',':
			continue
		else:
			print("ERROR")

	print(score)
