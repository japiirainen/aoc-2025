from collections import defaultdict

lines = open(0).read().splitlines()

points = [tuple(map(int, line.split(","))) for line in lines]

dists = sorted(
    ((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2, i, j)
    for i, (x1, y1, z1) in enumerate(points)
    for j, (x2, y2, z2) in enumerate(points)
    if i > j
)


uf = {i: i for i in range(len(points))}


def find(x: int) -> int:
    if x == uf[x]:
        return x
    uf[x] = find(uf[x])
    return uf[x]


def mix(x, y) -> None:
    uf[find(x)] = uf[y]


conns = 0

for t, (_d, i, j) in enumerate(dists):
    if t == 1000:
        sz = defaultdict(int)
        for x in range(len(points)):
            sz[find(x)] += 1
        s = sorted(sz.values())
        print(s[-1] * s[-2] * s[-3])
    if find(i) != find(j):
        conns += 1
        mix(i, j)
