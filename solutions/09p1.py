tiles = [tuple(map(int, line.split(","))) for line in open(0).read().splitlines()]

print(
    max(
        (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
        for i, (x1, y1) in enumerate(tiles)
        for x2, y2 in tiles[i + 1 :]
    )
)
