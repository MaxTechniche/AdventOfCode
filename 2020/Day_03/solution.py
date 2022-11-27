from time import time
from functools import reduce
from operator import mul

t1 = time()

with open("2020/Day_03/input", "r") as f:
    trees = f.read().splitlines()

width = len(trees[0])

slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
trees_hit_slopes = []

for slope in slopes:
    col = row = 0
    trees_hit = 0
    x, y = slope

    while True:
        try:
            if trees[row][col % width] == "#":
                trees_hit += 1
        except IndexError:
            trees_hit_slopes.append(trees_hit)
            if x == 1 and y == 3:
                print("Part 1:", trees_hit)
            break

        col += y
        row += x

print("Part 2:", reduce(mul, trees_hit_slopes))

print("Time:", time() - t1)  # .001
