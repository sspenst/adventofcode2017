def get_strongest_bridge(components, port):
    m = 0
    l = 0

    for c in components:
        if c[0] == port or c[1] == port:
            comps = components[:]
            comps.remove(c)
            if c[0] == port:
                length, strength = get_strongest_bridge(comps, c[1])
            else:
                length, strength = get_strongest_bridge(comps, c[0])
            
            length += 1
            strength += c[0] + c[1]

            if length > l:
                l = length
                m = strength
            elif length == l and strength > m:
                m = strength

    return l, m

components = [list(map(int, line.split("/"))) for line in open('input', 'r').read().strip().split("\n")]

print(get_strongest_bridge(components, 0))
