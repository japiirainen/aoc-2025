from scipy.optimize import linprog

lines = open(0).readlines()

type Machine = tuple[set[int], list[set[int]], tuple[int, ...]]

machines: list[Machine] = []

for line in lines:
    toggles, *buttons, counters = line.split()
    toggles = set(i for i, x in enumerate(toggles[1:-1]) if x == "#")
    moves = [set(map(int, b[1:-1].split(","))) for b in buttons]
    counters = tuple(map(int, counters[1:-1].split(",")))
    machines.append((toggles, moves, counters))


def solve(machine: Machine) -> int:
    _, moves, goals = machine
    c = [1] * len(moves)
    eq = [[i in m for m in moves] for i in range(len(goals))]
    return linprog(c, A_eq=eq, b_eq=goals, integrality=True).fun


print(sum(solve(machine) for machine in machines))
