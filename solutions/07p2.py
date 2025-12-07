from functools import cache

G = [[char for char in line] for line in open(0).read().splitlines()]

S = next(
    (r, c) for r, line in enumerate(G) for c, char in enumerate(line) if char == "S"
)

splitters = set(
    (r, c) for r, line in enumerate(G) for c, char in enumerate(line) if char == "^"
)


@cache
def score(r: int, c: int) -> int:
    if r + 1 == len(G):
        return 1
    if (r + 1, c) in splitters:
        return score(r + 1, c - 1) + score(r + 1, c + 1)
    return score(r + 1, c)


print(score(*S))
