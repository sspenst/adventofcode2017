import sys

input = 277678

# terrible memory management but it gets the job done
s = [[0 for x in range(200)] for y in range(200)]

x = 100
y = 100

s[x][y] = 1

size = 2

while 1:
    # loop through each side of the square
    for i in range(4):
        # loop through a side
        for j in range(size):
            # first step of a square goes to the right
            if i == 0 and j == 0:
                x += 1
            elif i == 0:
                y += 1
            elif i == 1:
                x -= 1
            elif i == 2:
                y -= 1
            elif i == 3:
                x += 1

            # add all surrounding squares
            s[x][y] = s[x-1][y] + \
                      s[x-1][y-1] + \
                      s[x][y-1] + \
                      s[x+1][y-1] + \
                      s[x+1][y] + \
                      s[x+1][y+1] + \
                      s[x][y+1] + \
                      s[x-1][y+1]

            if s[x][y] > input:
                print(s[x][y])
                sys.exit()
    size += 2
