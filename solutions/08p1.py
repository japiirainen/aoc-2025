import math

lines = open(0).read().splitlines()

points = [tuple(map(int, line.split(","))) for line in lines]

edges = sorted(
    [(i, j) for i in range(len(points)) for j in range(i + 1, len(points))],
    key=lambda x: math.hypot(*[a - b for a, b in zip(points[x[0]], points[x[1]])]),
)

parent = list(range(len(points)))


def root(x):
    if parent[x] == x:
        return x
    parent[x] = root(parent[x])
    return parent[x]


def merge(a, b):
    parent[root(a)] = root(b)


for a, b in edges[:1000]:
    merge(a, b)

sizes = [0] * len(points)

for point in range(len(points)):
    sizes[root(point)] += 1

sizes.sort(reverse=True)

print(sizes[0] * sizes[1] * sizes[2])
