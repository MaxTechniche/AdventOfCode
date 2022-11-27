from time import time

t1 = time()

with open("2021/Day_09/input") as f:
    heightmap = [list(map(int, list(line))) for line in f.read().splitlines()]

risk = 0

basin_starts = []


def check_neighbors(position):
    num = heightmap[position[0]][position[1]]
    dirs = [-1, 0, 1]
    for x in dirs:
        for y in dirs:
            if position[0]+x < 0 or position[1]+y < 0:
                continue
            elif abs(x) == abs(y):
                continue
            try:
                compare = heightmap[position[0] + x][position[1] + y]
                if compare <= num:
                    return False, num
            except IndexError:
                pass
    return True, num


for row in range(len(heightmap)):
    for col in range(len(heightmap[row])):
        val, height = check_neighbors([row, col])
        if val:
            basin_starts.append((row, col))
            risk += height + 1

print("Part 1: " + str(risk))

basin_values = []
visited = [[False for x in y] for y in heightmap]


def get_basin(basin_start):
    basin = [basin_start]
    p = 0
    while p < len(basin):
        dirs = [-1, 0, 1]
        for x in dirs:
            for y in dirs:
                if basin[p][0] + x < 0 or basin[p][1] + y < 0:
                    continue
                elif abs(x) == abs(y):
                    continue
                try:
                    if not visited[basin[p][0] + x][basin[p][1] + y]:
                        visited[basin[p][0] + x][basin[p][1]+y] = True
                        if heightmap[basin[p][0] + x][basin[p][1] + y] < 9:
                            basin.append((basin[p][0] + x, basin[p][1] + y))
                except IndexError:
                    pass

        p += 1

    return len(basin) - 1


for basin in basin_starts:
    basin_values.append(get_basin(basin))

ht = sorted(basin_values)[-3:]

print("Part 2: " + str(ht[0] * ht[1] * ht[2]))

print("Time:", time() - t1)
