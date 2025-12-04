rolls = {
    (r, c)
    for r, line in enumerate(open(0).read().splitlines())
    for c, char in enumerate(line)
    if char == "@"
}
ds = {(-1, -1), (0, -1), (1, -1), (-1, 0), (+1, 0), (-1, 1), (0, 1), (1, 1)}


def inaccessible(rolls: set[tuple[int, int]]):
    for r, c in rolls:
        if len(rolls & {(dr + r, dc + c) for dr, dc in ds}) >= 4:
            yield (r, c)


cleaned = rolls.copy()

while True:
    n = set(inaccessible(cleaned))
    if cleaned & n == cleaned:
        break
    cleaned = n

print(len(rolls - cleaned))
