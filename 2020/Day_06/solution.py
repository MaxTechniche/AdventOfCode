from time import time

t1 = time()

with open("2020/Day_06/input", "r") as f:
    groups = [group.split("\n") for group in f.read().split("\n\n")]

total1 = 0
total2 = 0
for group in groups:
    answer1 = set()
    answer2 = set(group[0])
    for person in group:
        person = set(person)
        answer1 = answer1.union(person)
        answer2 &= person
    total1 += len(answer1)
    total2 += len(answer2)

print("Part 1:", total1)
print("Part 2:", total2)
print("Time:", time() - t1)  # .007
