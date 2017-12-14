SIZE = 256

s = 'wenycdww-'

total = 0

for n in range(128):
    t = s + str(n)
    lengths = [ord(c) for c in t]
    lengths.extend([17, 31, 73, 47, 23])
    arr = [i for i in range(SIZE)]
    cur_pos = 0
    skip = 0

    for a in range(64):
        for length in lengths:
            # reverse order of length elements of arr
            for i in range(int(length/2)):
                ia = (i + cur_pos) % SIZE
                ib = (ia + length - 2*i - 1) % SIZE
                arr[ia], arr[ib] = arr[ib], arr[ia]

            cur_pos = (cur_pos + length + skip) % SIZE
            skip += 1

    dense_hash = [0] * 16

    for i in range(SIZE):
        dense_hash[int(i/16)] ^= arr[i]

    hex = ""

    for i in range(16):
        hex += "%0.2x" % dense_hash[i]
    
    total += "{0:b}".format(int(hex,16)).count('1')

print(total)
