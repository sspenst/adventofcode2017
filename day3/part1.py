import sys

input = 277678

dist = 0
size = 2
num = 1

while 1:
    # loop through each side of the square
    for i in range(4):
        # loop through the first half of a side
        for j in range(size>>1):
            # first step of a square increases the distance
            if i == 0 and j == 0:
                dist += 1
            else:
                dist -= 1
            num += 1
            if num == input:
                print(dist)
                sys.exit()
        # loop through the second half of a side
        for j in range(size>>1):
            dist += 1
            num += 1
            if num == input:
                print(dist)
                sys.exit()
    size += 2
