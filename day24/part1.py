def get_strongest_bridge(components, port):
    m = 0

    for c in components:
        if c[0] == port or c[1] == port:
            comps = components[:]
            comps.remove(c)
            if c[0] == port:
                strength = c[0] + c[1] + get_strongest_bridge(comps, c[1])
            else:
                strength = c[0] + c[1] + get_strongest_bridge(comps, c[0])
            if strength > m:
                m = strength

    return m

components = [list(map(int, line.split("/"))) for line in open('input', 'r').read().strip().split("\n")]

print(get_strongest_bridge(components, 0))
