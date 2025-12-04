rolls = {
    (r, c)
    for r, line in enumerate(open(0).read().splitlines())
    for c, char in enumerate(line)
    if char == "@"
}

ds = {(-1, -1), (0, -1), (1, -1), (-1, 0), (+1, 0), (-1, 1), (0, 1), (1, 1)}

print(sum(len(rolls & {(dr + r, dc + c) for dr, dc in ds}) < 4 for r, c in rolls))
