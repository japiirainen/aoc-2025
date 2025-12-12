import re

ans = 0

for line in list(open(0))[30:]:
    x, y, *n = map(int, re.findall(r"\d+", line))
    ans += x // 3 * y // 3 >= sum(n)

print(ans)
