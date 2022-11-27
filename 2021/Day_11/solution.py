from time import time
from pprint import pprint

t1 = time()

with open("2021/Day_11/input") as f:
    octos = [list(map(int, list(x))) for x in f.read().splitlines()]


total_flashes = 0
dirs = [-1, 0, 1]
step = 0
while True:
    flashed = [[False for x in y] for y in octos]

    inc = []
    for x in range(len(octos)):
        for y in range(len(octos[x])):
            octos[x][y] += 1
            if octos[x][y] > 9:
                flashed[x][y] = True
                for i in dirs:
                    for j in dirs:
                        # if i == j:
                        #     continue
                        if x+i < 0 or x+i >= len(octos) or y+j < 0 or y+j >= len(octos[0]):
                            continue
                        inc.append((x+i, y+j))
    pos = 0
    while pos < len(inc):
        a, b = inc[pos]
        octos[a][b] += 1
        if not flashed[a][b]:
            if octos[a][b] > 9:
                flashed[a][b] = True

                for i in dirs:
                    for j in dirs:
                        if a+i < 0 or a+i >= len(octos) or b+j < 0 or b+j >= len(octos[0]):
                            continue
                        inc.append((a+i, b+j))

        pos += 1
    step += 1

    current_flashes = 0
    for row in flashed:
        total_flashes += sum(row)
        current_flashes += sum(row)

    if current_flashes == 100:
        pprint(flashed)
        print(step)
        break

    octos = [[x*(x < 10) or 0 for x in y] for y in octos]

    if step == 100:
        print(total_flashes)


print("Time:", time() - t1)
