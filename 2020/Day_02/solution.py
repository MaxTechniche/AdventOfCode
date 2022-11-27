import time

t1 = time.time()

with open("2020/Day_02/input", "r") as f:
    passwords = f.readlines()

count1 = 0
count2 = 0

for password in passwords:
    min_max, letter, password = password.split()
    left, right = map(int, min_max.split("-"))
    letter = letter[:-1]

    # Part 1
    if left <= password.count(letter) <= right:
        count1 += 1

    # Part 2
    if (password[left - 1] == letter) ^ (password[right - 1] == letter):
        count2 += 1


print("Part 1:", count1)
print("Part 2:", count2)
print(time.time() - t1)  # .003
