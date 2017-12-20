class Particle():
    def __init__(self, p, v, a):
        self.p = list(map(int, p.split("=<")[1].split(">")[0].split(",")))
        self.v = list(map(int, v.split("=<")[1].split(">")[0].split(",")))
        self.a = list(map(int, a.split("=<")[1].split(">")[0].split(",")))

    def update(self):
        for i in range(3):
            self.v[i] += self.a[i]
            self.p[i] += self.v[i]

    def dist(self):
        return abs(self.a[0]) + abs(self.a[1]) + abs(self.a[2])

with open('input', 'r') as f:
    lines = f.read().strip().split("\n")

    particles = []

    for line in lines:
        p, v, a = line.split(", ")
        particles.append(Particle(p, v, a))

    m = particles[0].dist()
    idx = 0

    for i in range(len(particles)):
        if particles[i].dist() < m:
            m = particles[i].dist()
            idx = i

    print(idx)