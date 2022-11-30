from itertools import combinations

containers = sorted(list(map(int, open('AOC_2015\input').read().split('\n'))))
print(containers)

count = 0
for x in range(1, len(containers)+1):
    for perm in combinations(containers, x):
        if sum(perm) == 150:
            count += 1
    if count:
        break
print(count)