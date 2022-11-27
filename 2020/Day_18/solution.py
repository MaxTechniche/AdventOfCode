from time import time
import re
from math import prod

t1 = time()

with open("2020/Day_18/input") as f:
    lines = f.read().splitlines()


def evaluate(group):
    group = group.split(" ")
    num = int(group[0])
    times = False
    add = False
    for char in group[1:]:
        if not char:
            continue
        if times:
            num *= int(char)
        elif add:
            num += int(char)

        if char == "+":
            add = True
        else:
            add = False

        if char == "*":
            times = True
        else:
            times = False
    return str(num)


def swap(group):
    group = group.split("*")
    num = prod(int(evaluate(i.strip())) for i in group)
    return num


total1 = 0
for line in lines:
    # print(line)
    while True:
        pars = re.findall("(\([ \d+*]+\))", line)
        if len(pars) == 0:
            total1 += int(evaluate(line))
            break
        for par in pars:
            line = line.replace(par, evaluate(par[1:-1]))
print("Part 1:", total1)

total2 = 0
for line in lines:
    # print(line)
    while True:
        pars = re.findall("(\([ \d+*]+\))", line)
        if len(pars) == 0:
            total2 += int(swap(line))
            break
        for par in pars:
            line = line.replace(par, str(swap(par[1:-1])))


print("Part 2:", total2)

print("Time:", time() - t1)  # .02
