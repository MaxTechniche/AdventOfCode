from time import time
from pprint import pprint
from copy import deepcopy
import re

t1 = time()

with open("2020/Day_19/input") as f:
    r, m = f.read().split("\n\n")

rules = {}
for line in r.splitlines():
    left, right = line.split(":")
    left = " " + left + " "
    right = " " + right.strip(""""' """) + " "
    rules[left] = right

# rules = {line.split(":")[0]: line.split(":")[1] for line in r.splitlines()}

# pprint(rules)
# print()

temp_rules = deepcopy(rules)

while True:
    prev = rules[" 0 "]
    for rule in rules.keys():
        if rule in prev:
            n = " (" + rules[rule] + ") "
            # if "|" in rules[rule]:
            #     n = " (" + rules[rule] + ") "
            # else:
            #     n = rules[rule]
            rules[" 0 "] = rules[" 0 "].replace(rule, n)
    if prev == rules[" 0 "]:
        break

rule_0 = "".join(rules[" 0 "].split())

total = 0
for message in m.splitlines():
    print
    if re.match("^" + rule_0 + "$", message):
        total += 1
# print(rule_0)
print("Part 1:", total)

rules = temp_rules
rules[" 8 "] = " 42 {1,} "
rules[" 11 "] = " 42 31  "

prev_total = 0
total = 0
count = 0
while count <= 10:
    for rule in rules.keys():
        if rule in rules[" 0 "]:
            if rules[rule] in [" a ", " b "]:
                n = rules[rule]
            else:
                n = " (" + rules[rule] + ") "
            # if "|" in rules[rule]:
            #     n = " (" + rules[rule] + ") "
            # else:
            #     n = rules[rule]
            rules[" 0 "] = rules[" 0 "].replace(rule, n)
    total = 0
    for message in m.splitlines():
        if re.match("^" + "".join(rules[" 0 "].split()) + "$", message):
            total += 1
    print(total)
    if total == prev_total:
        count += 1
    else:
        count = 0
    prev_total = total

rule_0 = "".join(rules[" 0 "].split())

print(rule_0)
# print(re.sub("\d", "", rule_0))
print("Part 2:", total)

print("Time:", time() - t1)
