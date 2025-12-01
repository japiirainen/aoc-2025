here = 50
x = 0

sym = lambda x: (-x) % 100

for d, n in ((x[0], int(x[1:])) for x in (x.strip() for x in open(0).readlines())):
    if d == "R":
        zeros, heree = divmod(here + n, 100)
        here = heree
        x += zeros
    if d == "L":
        zeros, heree = divmod(sym(here) + n, 100)
        here = sym(heree)
        x += zeros

print(x)
