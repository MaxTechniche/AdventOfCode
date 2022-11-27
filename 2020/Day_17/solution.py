from time import time
from pprint import pprint
from collections import defaultdict
from copy import deepcopy

t1 = time()

cuboid = defaultdict(bool)

with open("2020/Day_17/input") as f:
    for y, line in enumerate(f.read().splitlines()):
        for z, char in enumerate(line):
            cuboid[f"0:{y}:{z}"] = True if char == "#" else False

min_x = min_y = min_z = -1
max_x = 2
max_y = y + 2
max_z = z + 2


def get_neighbors(x, y, z):
    l = [-1, 0, 1]
    total = 0
    for i in l:
        for j in l:
            for k in l:
                if i == j == k == 0:
                    continue
                total += 1 * cuboid[f"{x+i}:{y+j}:{z+k}"]

    return total


step = 0
while step < 6:
    next_cuboid = deepcopy(cuboid)
    for x in range(min_x, max_x):
        for y in range(min_y, max_y):
            for z in range(min_z, max_z):
                alive_neighbors = get_neighbors(x, y, z)
                if alive_neighbors == 3:
                    next_cuboid[f"{x}:{y}:{z}"] = True
                elif alive_neighbors == 2 and cuboid[f"{x}:{y}:{z}"]:
                    next_cuboid[f"{x}:{y}:{z}"] = True
                else:
                    next_cuboid[f"{x}:{y}:{z}"] = False

    cuboid = deepcopy(next_cuboid)

    min_x -= 1
    min_y -= 1
    min_z -= 1
    max_x += 1
    max_y += 1
    max_z += 1
    step += 1


print("Part 1:", sum(cuboid.values()))

# Part 2 Same. Just add w
cuboid = defaultdict(bool)

with open("2020/Day_17/input") as f:
    for y, line in enumerate(f.read().splitlines()):
        for z, char in enumerate(line):
            cuboid[f"0:{y}:{z}:0"] = True if char == "#" else False

min_x = min_y = min_z = min_w = -1
max_x = 2
max_y = y + 2
max_z = z + 2
max_w = 2


def get_neighbors(x, y, z, w):
    l = [-1, 0, 1]
    total = 0
    for i in l:
        for j in l:
            for k in l:
                for h in l:
                    if i == j == k == h == 0:
                        continue
                    total += 1 * cuboid[f"{x+i}:{y+j}:{z+k}:{w+h}"]

    return total


step = 0
while step < 6:
    next_cuboid = deepcopy(cuboid)
    for x in range(min_x, max_x):
        for y in range(min_y, max_y):
            for z in range(min_z, max_z):
                for w in range(min_w, max_w):
                    alive_neighbors = get_neighbors(x, y, z, w)
                    if alive_neighbors == 3:
                        next_cuboid[f"{x}:{y}:{z}:{w}"] = True
                    elif alive_neighbors == 2 and cuboid[f"{x}:{y}:{z}:{w}"]:
                        next_cuboid[f"{x}:{y}:{z}:{w}"] = True
                    else:
                        next_cuboid[f"{x}:{y}:{z}:{w}"] = False

    cuboid = deepcopy(next_cuboid)

    min_x -= 1
    min_y -= 1
    min_z -= 1
    min_w -= 1
    max_x += 1
    max_y += 1
    max_z += 1
    max_w += 1
    step += 1


print("Part 2:", sum(cuboid.values()))


print("Time:", time() - t1)  # 12
