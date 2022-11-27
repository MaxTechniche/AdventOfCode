from time import time

t1 = time()

with open("2020/Day_05/input", "r") as f:
    people = f.read().splitlines()

seat_ids = set()
for person in people:
    bin_string = "".join(["0" if char in "FL" else "1" for char in person])
    row = int(bin_string[:7], 2)
    col = int(bin_string[7:], 2)
    num = row * 8 + col
    seat_ids.add(num)

print("Part 1:", max(seat_ids))
for num in range(min(seat_ids), max(seat_ids)):
    if num not in seat_ids:
        print("Part 2:", num)
        break

print("Time:", time() - t1)  # .003
