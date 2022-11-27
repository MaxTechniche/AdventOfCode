from time import time
from copy import deepcopy

t1 = time()

with open("2020/Day_11/input") as f:
    og_tiles = [list(tile) for tile in f.read().splitlines()]


tiles = deepcopy(og_tiles)


def check_sight(x, y, i, j):
    while True:
        x += i
        y += j
        if x < 0 or y < 0:
            return 0
        try:
            if tiles[x][y] in ["L", "#"]:
                if tiles[x][y] == "#":
                    return 1
                return 0
        except IndexError:
            return 0


part2 = False


def get_next(x, y, tile):
    total = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i == j == 0:
                continue
            if part2:
                total += check_sight(x, y, i, j)
            else:
                if x + i < 0 or y + j < 0:
                    continue
                try:
                    if tiles[x + i][y + j] == "#":
                        total += 1
                except IndexError:
                    pass
    # print(tile, total)

    if tile == "#" and total >= 4 + int(part2):
        return "L"
    if tile == "L" and total == 0:
        return "#"
    return tile


def count_occupied(seats):
    total = 0
    for row in seats:
        total += row.count("#")
    return total


iters = 0
while True:
    iters += 1
    temp = deepcopy(tiles)

    for x in range(len(tiles)):
        for y in range(len(tiles[x])):
            temp[x][y] = get_next(x, y, tiles[x][y])

    # print(*["".join(row) for row in temp], sep="\n")
    # print()
    if temp == tiles:
        print("Part 1:", count_occupied(temp), "Iterations:", iters)
        part2 = True
        break

    tiles = temp

tiles = deepcopy(og_tiles)

iters = 0
while True:
    iters += 1
    temp = deepcopy(tiles)

    for x in range(len(tiles)):
        for y in range(len(tiles[x])):
            temp[x][y] = get_next(x, y, tiles[x][y])

    if temp == tiles:
        print("Part 2:", count_occupied(temp), "Iterations:", iters)
        break

    tiles = temp

print("Time:", time() - t1)  # 9+
