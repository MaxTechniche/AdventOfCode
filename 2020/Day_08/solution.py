from time import time
from copy import deepcopy

t1 = time()

base = {}
with open("2020/Day_08/input", "r") as f:
    for x, line in enumerate(f.read().splitlines()):
        code, val = line.split()
        base[x] = {"code": code, "value": int(val), "visited": False}

part1 = True


def follow(swap=None):
    codes = deepcopy(base)
    acc = 0
    pos = 0

    if swap != None:
        codes[swap]["code"] = "jmp" if codes[swap]["code"] == "nop" else "nop"

    while True:
        if pos not in codes:
            return acc

        if codes[pos]["visited"]:
            if part1:
                print("Part 1:", acc)
            return

        codes[pos]["visited"] = True

        if codes[pos]["code"] == "acc":
            acc += codes[pos]["value"]
            pos += 1

        elif codes[pos]["code"] == "jmp":
            pos += codes[pos]["value"]

        elif codes[pos]["code"] == "nop":
            pos += 1

        else:
            print(f'ERROR: code {codes[pos]["code"]} not found!')


pos = 0

while True:
    if part1:
        follow()
        part1 = False

    if pos not in base:
        print("Error: No route found")
        break

    if base[pos]["code"] in ["jmp", "nop"]:
        if val := follow(pos):
            print("Part 2:", val)
            break
    pos += 1

print("Time:", time() - t1)  # .55
