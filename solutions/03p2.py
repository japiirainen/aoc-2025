S = 0

for bank in open(0).read().splitlines():
    k, s = 0, ""
    for i in range(12):
        k = max(range(k, len(bank) - 12 + i + 1), key=lambda x: bank[x])
        s += bank[k]
        k += 1
    S += int(s)

print(S)
