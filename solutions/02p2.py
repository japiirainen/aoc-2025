import math
import textwrap
import itertools
import functools


@functools.cache
def proper_divisors(n: int) -> list[int]:
    divs = [1]
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divs.extend([i, n // i])
    return list(set(divs))


x = 0

for lo, hi in [x.split("-") for x in open(0).read().strip().split(",")]:
    for k in range(int(lo), int(hi) + 1):
        s = str(k)
        for d in proper_divisors(len(s)):
            chunks = textwrap.wrap(s, d)
            if len(chunks) > 1 and all(a == b for a, b in itertools.pairwise(chunks)):
                x += k
                break

print(x)
