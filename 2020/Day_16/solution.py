from time import time
from math import prod
from pprint import pprint
import re

t1 = time()


def merge(ranges):
    _ranges = [ranges[0]]
    for _range in ranges[1:]:
        mn, mx = _range
        for i, (l, r) in enumerate(_ranges):
            if l <= mn <= r:
                _ranges[i][1] = max(r, mx)
            elif l <= mx <= r:
                _ranges[i][0] = min(l, mn)
            else:
                continue
            _ranges = merge(_ranges)
            break
        else:
            _ranges.append([mn, mx])

    return _ranges


with open("2020/Day_16/input") as f:
    lines = f.read().split("\n\n")

all_ranges = merge(
    [list(map(int, x.split("-"))) for x in re.findall("\d+-\d+", lines[0])]
)
nearby_tickets = lines[2].split("\n")[1:]

nt_1 = list(map(int, ",".join(nearby_tickets).split(",")))

invalid_tickets = set()

lines[0] = lines[0].splitlines()

pos = 0
num_rules = len(lines[0])

total1 = 0
for val in nt_1:
    for l, r in all_ranges:
        if l <= val <= r:
            break
    else:
        total1 += val
        invalid_tickets.add(pos // num_rules)
    pos += 1

print("Part 1:", total1)

each_range = {}
for rule in lines[0]:
    rule, ranges = rule.split(":")
    each_range[rule] = merge(
        [list(map(int, x.split("-"))) for x in re.findall("\d+-\d+", ranges)]
    )


possibles = list(each_range.keys())
actual_poss = [[val for val in possibles] for _ in range(num_rules)]
for i, x in enumerate(nt_1):
    ir = divmod(i, num_rules)
    if ir[0] in invalid_tickets:
        continue
    for k, rule in enumerate(possibles):
        ranges = each_range[rule]
        for l, r in ranges:
            if l <= x <= r:
                break
        else:
            if rule in actual_poss[ir[1]]:
                actual_poss[ir[1]].remove(rule)

actual_poss = [[a, b] for a, b in enumerate(actual_poss)]
actual_poss.sort(key=lambda x: len(x[1]))


final = []

while actual_poss:
    for x in range(1, len(actual_poss)):
        try:
            actual_poss[x][1].remove(actual_poss[0][1][0])
        except ValueError:
            pass
    final.append([actual_poss[0][0], actual_poss[0][1][0]])
    actual_poss = actual_poss[1:]

mine = list(map(int, lines[1].splitlines()[1].split(",")))


departures = [mine[s] for s, name in final if "departure" in name]

print("Part 2:", prod(departures))

print("Time:", time() - t1)  # .06
