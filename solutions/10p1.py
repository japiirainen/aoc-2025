from collections import deque

lines = open(0).readlines()

type Machine = tuple[set[int], list[set[int]], tuple[int, ...]]

machines: list[Machine] = []

for line in lines:
    toggles, *buttons, counters = line.split()
    toggles = set(i for i, x in enumerate(toggles[1:-1]) if x == "#")
    moves = [set(map(int, b[1:-1].split(","))) for b in buttons]
    counters = tuple(map(int, counters[1:-1].split(",")))
    machines.append((toggles, moves, counters))


def solve_machine(machine: Machine) -> int:
    goal, moves, _ = machine

    Q = deque([(set(), 0)])

    seen = set()

    while Q:
        curr, steps = Q.popleft()
        if curr == goal:
            return steps
        for m in moves:
            newset = curr ^ m
            if newset in seen:
                continue
            seen.add(frozenset(newset))
            Q.append((newset, steps + 1))

    raise ValueError("no solution.")


print(sum(solve_machine(machine) for machine in machines))
