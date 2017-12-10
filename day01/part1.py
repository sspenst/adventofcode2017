with open('input', 'r') as f:
    read_data = f.read().strip()
    total = 0;
    prev_char = read_data[len(read_data)-1]
    for i in range(len(read_data)):
        if prev_char == read_data[i]:
            total += int(read_data[i])
        prev_char = read_data[i]
    print(total)
