SIZE = 256

with open('input', 'r') as f:
	lengths = list(map(int, f.read().strip().split(',')))
	arr = [i for i in range(SIZE)]
	cur_pos = 0
	skip = 0

	for length in lengths:
		# reverse order of length elements of arr
		for i in range(int(length/2)):
			ia = (i + cur_pos) % SIZE
			ib = (ia + length - 2*i - 1) % SIZE
			arr[ia], arr[ib] = arr[ib], arr[ia]

		cur_pos = (cur_pos + length + skip) % SIZE
		skip += 1

	print(arr[0] * arr[1])
