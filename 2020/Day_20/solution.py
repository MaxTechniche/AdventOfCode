from time import time
from pprint import pprint

t1 = time()


def side(line):
    f = []
    for i, v in enumerate(line):
        if v == "#":
            f.append(i)
    b = [len(line) - 1 - x for x in f]
    new_side = list(zip(f, b))
    return new_side


def get_sides(group):
    group = [list(line) for line in group]
    sides = []
    sides.append(side(group[0]))
    sides.append(side([group[x][-1] for x in range(len(group))]))
    sides.append(side(group[-1]))
    sides.append(side([group[x][0] for x in range(len(group))]))

    return sides


tiles = {}

with open("2020/Day_20/input") as f:
    groups = []
    count = 0
    for group in f.read().split("\n\n"):
        count += 1
        group = group.splitlines()
        id = int(group[0][0:-1].split()[1])
        sides = [id, get_sides(group[1:])]
        tiles[id] = sides

pprint(tiles)
print(count)
print("Time:", time() - t1)
