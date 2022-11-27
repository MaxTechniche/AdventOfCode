from time import time

print('Running...')

t1 = time()

with open("2021/Day_06/input") as f:
    fish = f.read()

lanternfish_count = {}
for i in range(9):
    lanternfish_count[i] = fish.count(str(i))

lanternfish_change = {x: 0 for x in range(9)}
lanternfish_timers = list(range(8, -1, -1))

current_day = 0
while current_day < 256:
    for timer in lanternfish_timers:
        if timer == 0:
            lanternfish_change[6] += lanternfish_count[timer]
            lanternfish_change[8] += lanternfish_count[timer]
        else:
            lanternfish_change[timer-1] += lanternfish_count[timer]

    lanternfish_count = lanternfish_change
    lanternfish_change = {x: 0 for x in range(9)}

    current_day += 1
    if current_day == 80:
        print("Part 1:", sum([y for x, y in lanternfish_count.items()]))

print("Part 2:", sum([y for x, y in lanternfish_count.items()]))

print("Time:", time() - t1)
