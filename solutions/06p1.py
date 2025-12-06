lines = [line.split() for line in open(0).read().splitlines()]

print(sum(eval(op.join(nums)) for *nums, op in list(zip(*lines))))
