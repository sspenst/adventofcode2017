with open('input', 'r') as f:
    read_data = f.read().strip()
    total = 0;
    half = int(len(read_data)/2)
    for i in range(half):
        if read_data[i] == read_data[half+i]:
            total += int(read_data[i])
    print(total*2)
