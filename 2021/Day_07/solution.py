from time import time

t1 = time()

with open("2021/Day_07/input") as f:
    crabs = list(map(int, f.read().split(',')))

total_fuel = 0
median = sorted(crabs)[len(crabs)//2]

for crab in crabs:
    total_fuel += abs(median - crab)

print("Part 1:", total_fuel)

total_fuel = 0
mean = sum(crabs) / len(crabs)

for crab in crabs:
    dist = abs(mean - crab)
    total_fuel += dist * (dist + 1) // 2

print("Part 2:", total_fuel)

print("Time:", time() - t1)


# 1 = 1
# 2 = 3
# 3 = 6
# 4 = 10
# 5 = 15
