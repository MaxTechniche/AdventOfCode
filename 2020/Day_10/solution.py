from time import time
from collections import defaultdict

t1 = time()

with open("2020/Day_10/input") as f:
    lines = sorted(map(int, f.read().splitlines()))

differences = defaultdict(int)

device = max(lines) + 3

current = 0
for line in lines + [device]:
    differences[line - current] += 1
    current = line

print("Part 1:", differences[1] * differences[3])

adapters = lines[::-1]
memo = {}


def get_count(adapter, bigger_adapters=None):
    """ Get number of ways adapter can be connected to larger adapters. """
    if not bigger_adapters:
        return 0
    if len(bigger_adapters) == 1:
        return 1
    if adapter in memo:
        return memo[adapter]

    total = 0
    for i, adapt in enumerate(bigger_adapters):
        if 0 < adapt - adapter <= 3:
            memo[adapt] = get_count(adapt, bigger_adapters[i + 1 :])
            total += memo[adapt]

    return total


print("Part 2:", get_count(0, lines))

print("Time:", time() - t1)  # .0015
