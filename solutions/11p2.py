from functools import cache

G = {k[:-1]: v for k, *v in map(str.split, open(0))} | {"out": []}


@cache
def count(here, there):
    return here == there or sum(count(n, there) for n in G[here])


print(
    count("svr", "dac") * count("dac", "fft") * count("fft", "out")
    + count("svr", "fft") * count("fft", "dac") * count("dac", "out")
)
