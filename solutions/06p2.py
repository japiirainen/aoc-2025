grid = [line.strip("\n") for line in open(0)]

group, groups = [], []

for col in list(zip(*grid)):
    if set(col) == {" "}:
        groups.append(group)
        group = []
    else:
        group.append(col)

groups.append(group)

print(
    sum(
        eval(group[0][-1].join("".join(line[:-1]) for line in group))
        for group in groups
    )
)
