here = 50
x = 0

for n in (
    int(x[1:]) if x[0] == "R" else -int(x[1:])
    for x in (x.strip() for x in open(0).readlines())
):
    here = (here + n) % 100
    x += here == 0

print(x)
