data = {}

found = []

def count(n):
    found.append(n)

    for i in data[n]:
        if i not in found:
            count(i)

with open('input', 'r') as f:
    lines = f.read().strip().split("\n")

    for line in lines:
        s = line.split(" <-> ")
        data[int(s[0])] = list(map(int, s[1].split(", ")))

    total = 0

    for i in range(len(data)):
        if i not in found:
            count(i)
            total += 1

    print(total)