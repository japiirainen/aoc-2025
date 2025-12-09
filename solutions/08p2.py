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


circuits = len(points)

for a, b in edges:
    if root(a) == root(b):
        continue
    merge(a, b)
    circuits -= 1
    if circuits == 1:
        print(points[a][0] * points[b][0])
        break
