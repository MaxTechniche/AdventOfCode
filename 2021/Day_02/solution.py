from time import time

t1 = time()

with open("2021/Day_02/input") as f:
    lines = f.read().splitlines()

horizontal_position = 0
aim = 0
part1_depth = 0
part2_depth = 0

for line in lines:
    line = line.split(' ')
    if line[0] == 'forward':
        horizontal_position += int(line[1])
        part2_depth += aim * int(line[1])
    elif line[0] == 'down':
        part1_depth += int(line[1])
        aim += int(line[1])
    elif line[0] == 'up':
        part1_depth -= int(line[1])
        aim -= int(line[1])

print("Part 1:")
print(horizontal_position * part1_depth)
print("Part 2:")
print(horizontal_position * part2_depth)

print("Time:", time() - t1)


#
#
#
#
#
#
#
#
#
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

# with open("2021/Day_02/input") as f:
#     lines = [x.split(" ") for x in f.read().splitlines()]

# hor = 0
# ver = 0

# for direction, unit in lines:
#     if direction == "forward":
#         hor += int(unit)
#     elif direction == "down":
#         ver += int(unit)
#     elif direction == "up":
#         ver -= int(unit)

# print("Horizontal:", hor)
# print("Vertical:", ver)
# print(hor*ver)


# print("Time:", time() - t1)

# # Part 2
# t1 = time()

# with open("2021/Day_02/input") as f:
#     lines = [x.split(" ") for x in f.read().splitlines()]

# hor = 0
# ver = 0
# aim = 0

# for direction, unit in lines:
#     if direction == "forward":
#         hor += int(unit)
#         ver += int(unit) * aim
#     elif direction == "down":
#         aim += int(unit)
#     elif direction == "up":
#         aim -= int(unit)

# print("Horizontal:", hor)
# print("Vertical:", ver)
# print(hor*ver)


# print("Time:", time() - t1)
