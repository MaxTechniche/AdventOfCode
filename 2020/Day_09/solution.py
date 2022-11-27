from time import time

t1 = time()


with open("2020/Day_09/input") as f:
    lines = list(map(int, f.read().splitlines()))

print(len(lines))
part1 = True

preamble = lines[:25]


def find_sum(number):
    for i in range(len(preamble) - 1):
        for j in range(i + 1, len(preamble)):
            if i != j:
                if preamble[i] + preamble[j] == number:
                    return True


pos = 25
p1_int = None

while pos < len(lines):
    if not find_sum(lines[pos]):
        if part1:
            print("Part 1:", lines[pos])
            part1 = False
            p1_int = lines[pos]
            break
    del preamble[0]
    preamble.append(lines[pos])
    pos += 1

pos = -1

numbers = []
while True:
    pos += 1

    if pos >= len(lines):
        print("ERROR: No contiguous sum found")
        break

    numbers.append(lines[pos])

    while sum(numbers) > p1_int:
        numbers = numbers[1:]

    if sum(numbers) == p1_int and len(numbers) > 1:
        print(
            "Part 2:",
            max(numbers) + min(numbers),
        )
        print("  Length of numbers:", len(numbers))
        break


print("Time:", time() - t1)  # .016
