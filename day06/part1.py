with open('input', 'r') as f:
	bank = list(map(int, f.read().strip().split("\t")))
	prev_banks = []
	prev_banks.append(' '.join(list(map(str, bank))))
	len_bank = len(bank)
	cycle = 0

	while 1:
		cycle += 1
		
		max = 0
		index = 0
		for i in range(len_bank):
			if bank[i] > max:
				max = bank[i]
				index = i

		blocks = bank[index]
		bank[index] = 0
		
		while blocks > 0:
			index += 1
			index %= len_bank
			blocks -= 1
			bank[index] += 1

		new_bank = ' '.join(list(map(str, bank)))
		if new_bank in prev_banks:
			print(cycle)
			break
		else:
			prev_banks.append(new_bank)
