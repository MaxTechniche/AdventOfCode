from time import time

t1 = time()

get_1 = 2020
get_2 = 30_000_000

with open("2020/Day_15/input") as f:
    starting = list(map(int, f.read().split(",")))

number_dict = {num: i for i, num in enumerate(starting[:-1])}

x = len(starting) - 1
num = starting[x]
while x < 30000000:
    if x == get_1 - 1:
        print("Part 1:", num)
    if x == get_2 - 1:
        print("Part 2:", num)
    if num in number_dict:
        dist = x - number_dict[num]
        number_dict[num] = x
        num = dist
    else:
        number_dict[num] = x
        num = 0
    x += 1

print("Time:", time() - t1)  # 30
