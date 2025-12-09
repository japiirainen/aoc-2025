from shapely.geometry.polygon import Polygon
from itertools import combinations


tiles = [tuple(map(int, line.split(","))) for line in open(0).read().splitlines()]

poly = Polygon(tiles)

print(
    max(
        ((abs(p1[1] - p2[1]) + 1) * (abs(p1[0] - p2[0]) + 1))
        for p1, p2 in combinations(tiles, 2)
        if poly.contains(Polygon([p1, (p2[0], p1[1]), p2, (p1[0], p2[1])]))
    )
)
