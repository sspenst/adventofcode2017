with open('input', 'r') as f:
    maze = list(map(int, f.read().strip().split("\n")))
    index = 0
    steps = 0
    while 1:
        steps += 1
        offset = maze[index]
        if offset >= 3:
            maze[index] -= 1
        else:
            maze[index] += 1
        index += offset
        if index < 0 or index >= len(maze):
            print(steps)
            break
