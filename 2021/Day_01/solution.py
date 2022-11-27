from time import time

t1 = time()

with open("2021/Day_01/input") as f:
    lines = list(map(int, f.read().splitlines()))

total_increases = 0
last = lines[0]

for num in lines[1:]:
    if num > last:
        total_increases += 1
    last = num

print(total_increases)

print("Part 2:")
total_increases = 0
last = sum(lines[0:3])

for x in range(3, len(lines)+1):
    num = sum(lines[x-3:x])
    if num > last:
        total_increases += 1
    last = num

print(total_increases)
print("Time:", time() - t1)

#
#
##
#
#
#
##
#
#
#
#
#
#
#
#
#
# from time import time

# t1 = time()

# with open("2021/Day_01/input") as f:
#     lines = [int(x) for x in f.read().splitlines()]
#     #Part 2
#     lines = [sum(lines[x-2:x+1]) for x in range(2, len(lines))]
#     #Part 2

# prev_depth = lines[0]
# incs = 0

# for depth in lines:
#     if depth > prev_depth:
#         incs += 1
#     prev_depth = depth

# print(incs)

# print("Time:", time() - t1)
