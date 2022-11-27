import re
from time import time
from pprint import pprint
from itertools import product

# from collections import defaultdict

t1 = time()

with open("2020/Day_14/input") as f:
    instructions = f.read().splitlines()


def set_bits(value, mask, replace_list):
    value = bin(value)[2:]
    value = list(value.zfill(36))
    for i, val in enumerate(mask):
        if val in replace_list:
            value[i] = val
    return "".join(value)


memory = {}
memory2 = {}


def set_bits_2(value, mask, address):
    address = set_bits(address, mask, "X1").replace("X", "{}")

    xs = product("01", repeat=address.count("{}"))
    for combo in xs:
        memory2[address.format(*combo)] = value


for instruction in instructions:
    if instruction[:4] == "mask":
        mask = instruction[7:]
        continue
    address, value = map(int, re.findall("\d+", instruction))
    memory[address] = set_bits(value, mask, "01")
    set_bits_2(value, mask, address)

total = 0
for val in memory.values():
    total += int(val, 2)
print("Part 1:", total)

total = 0
for val in memory2.values():
    total += val
print("Part 2:", total)

print("Time:", time() - t1)  # .12
