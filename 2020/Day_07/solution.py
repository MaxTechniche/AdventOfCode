from time import time
import re

t1 = time()


def flatten(lst):
    lst_copy = []
    for item in lst:
        lst_copy.extend(item)
    return lst_copy


def get(number):
    if number:
        return int(number)
    return 0


with open("2020/Day_07/input", "r") as f:
    bag_rules = f.read().splitlines()

bags = {}
for big_bag in bag_rules:
    main, contents = big_bag.split(" bags contain ")
    bags[main] = [
        (get(num), sub_bag)
        for num, sub_bag in re.findall("(\d*) ([A-z ]+) bag", contents)
    ]

poss = set(["shiny gold"])

x = len(poss)
while True:
    for bag, contents in bags.items():
        for c in poss:
            if c in [b[1] for b in contents]:
                poss.add(bag)
                break
    if x == len(poss):
        break
    x = len(poss)

print("Part 1:", len(poss) - 1)


bags["other"] = []
shiny_contains = flatten([[colors] * num for num, colors in bags["shiny gold"]])
pos = -1

while True:
    pos += 1
    if pos >= len(shiny_contains):
        break
    next_bag = flatten([colors] * num for num, colors in bags[shiny_contains[pos]])
    shiny_contains.extend(next_bag)

print("Part 2:", len(shiny_contains) - shiny_contains.count("other"))

print("Time:", time() - t1)  # .33
