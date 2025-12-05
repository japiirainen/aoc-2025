a, b = open(0).read().split("\n\n")

fresh = [tuple(map(int, r.split("-"))) for r in a.splitlines()]

ids = tuple(map(int, b.splitlines()))

print(sum(any(l <= id <= h for (l, h) in fresh) for id in ids))
