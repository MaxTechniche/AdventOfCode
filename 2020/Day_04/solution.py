from pprint import pprint
from time import time
import re

t1 = time()

with open("2020/Day_04/input", "r") as f:
    passports = [
        dict(code.split(":") for code in port.split())
        for port in f.read().split("\n\n")
    ]


def validate_height(height):
    return (height[-2:] == "cm" and 150 <= int(height[:-2]) <= 193) or (
        height[-2:] == "in" and 59 <= int(height[:-2]) <= 76
    )


def validate(passport):
    try:
        if (
            1290 <= int(passport["byr"]) <= 2002
            and 2010 <= int(passport["iyr"]) <= 2020
            and 2020 <= int(passport["eyr"]) <= 2030
            and validate_height(passport["hgt"])
            and re.match("^#[0-9a-f]{6}$", passport["hcl"])
            and passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
            and re.match("^[0-9]{9}$", passport["pid"])
        ):
            return True
    except KeyError:
        return False


total1 = 0
total2 = 0
for pp in passports:
    if len(pp) == 8:
        total1 += 1
    if len(pp) == 7 and "cid" not in pp:
        total1 += 1
    if validate(pp):
        total2 += 1


print("Part 1:", total1)
print("Part 2:", total2)
print("Time:", time() - t1)  # .004
