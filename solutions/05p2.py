a, _ = open(0).read().split("\n\n")

fresh = [tuple(map(int, r.split("-"))) for r in a.splitlines()]

ans = curr = 0

for l, h in sorted(fresh):
    start = max(l, curr + 1)
    ans += max(0, h - start + 1)
    curr = h

print(ans)
