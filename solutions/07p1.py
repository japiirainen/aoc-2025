from collections import deque

G = [[char for char in line] for line in open(0).read().splitlines()]

S = next(
    (r, c) for r, line in enumerate(G) for c, char in enumerate(line) if char == "S"
)

splitters = set(
    (r, c) for r, line in enumerate(G) for c, char in enumerate(line) if char == "^"
)

Q, splits, seen = deque([S]), 0, {S}

while Q:
    cr, cc = Q.popleft()

    if (cr, cc) in splitters:
        splits += 1

    for dr, dc in [(0, 1), (0, -1)] if (cr, cc) in splitters else [(1, 0)]:
        nr, nc = cr + dr, cc + dc

        if (nr, nc) in seen:
            continue

        if not (0 <= nr < len(G)):
            continue

        seen |= {(nr, nc)}
        Q.append((nr, nc))

print(splits)
