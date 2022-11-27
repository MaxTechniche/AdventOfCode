from copy import deepcopy

lights = [[True if x == '#' else False for x in y] for y in open('AOC_2015\day18.txt').read().split('\n')]

def get_num_neighbors(x, y, lights):
    num_neighbors = 0
    nums = [-1, 0, 1]
    for a in nums:
        for b in nums:
            if x+a < 0 or b+y < 0:
                continue
            elif a == b == 0:
                continue
            try:
                if lights[x+a][y+b]:
                    num_neighbors += 1
            except IndexError:
                pass
    return num_neighbors

for step in range(100):
    new_lights = []
    for x in range(len(lights)):
        row = []
        for y in range(len(lights[x])):
            a = get_num_neighbors(x, y, lights)
            if lights[x][y]:
                if a == 3 or a == 2:
                    row.append(True)
                else:
                    row.append(False)
            else:
                if a == 3:
                    row.append(True)
                else:
                    row.append(False)
        new_lights.append(row)
    lights = deepcopy(new_lights)
    # print(*(''.join(['#' if r else '.' for r in l]) for l in lights), sep='\n')
    # print()

total = 0
for x in lights:
    total += x.count(True)
print(total)