x = 0

for lo, hi in [x.split("-") for x in open(0).read().strip().split(",")]:
    for k in range(int(lo), int(hi) + 1):
        s = str(k)
        if len(s) % 2 != 0:
            continue
        a, b = s[: len(s) // 2], s[len(s) // 2 :]
        x += k if a == b else 0

print(x)
