from time import time
import re
from pprint import pprint
import math

t1 = time()


def intify(val):
    if val[1] == "x":
        return val
    return val[0], int(val[1])


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


def get_dist(busses):
    busses = busses[::-1]
    bus = 1
    step = busses[0][1]
    check = 0
    while bus < len(busses):
        distance = busses[bus - 1][0] - busses[bus][0]
        while True:
            n = check - distance
            # print(check, n, distance, step)
            if n % busses[bus][1] == 0:
                print(f"Valid order last {bus+1} busses starting at {n}")
                break
            check += step
        check = n
        step = lcm(step, busses[bus][1])
        bus += 1

    return step


with open("2020/Day_13/input") as f:
    file = f.readlines()
    early_time = int(file[0])
    busses = list(enumerate(map(int, re.findall("(\d+)", file[1]))))
    busses_p2 = list(map(intify, enumerate(file[1].split(","))))
    busses_p2 = [x for x in busses_p2 if x[1] != "x"]

print(early_time)
print(busses)

print()

busses = [(bus, bus - (early_time % bus)) for i, bus in busses]
busses.sort(key=lambda x: (x[1], -x[0]))

print("Part 1:", busses[0][0] * busses[0][1])

print()
# print()
# print(busses_p2)


print()
print("Part 2:", get_dist(busses_p2))

print("Time:", time() - t1)  # .001
