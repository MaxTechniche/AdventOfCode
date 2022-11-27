from time import time

t1 = time()

with open("2021/Day_08/input") as f:
    displays = f.read().splitlines()

part_1_unique = 0

for display in displays:
    code, output = display.split(' | ')
    for num in output.split(' '):
        if len(num) in [2, 3, 4, 7]:
            part_1_unique += 1

print("Part 1: " + str(part_1_unique))

# Part 2
summed_output = 0

for display in displays:
    code, output = display.split(' | ')

    code = sorted(code.split(' '), key=len)

    one = code[0]
    seven = code[1]
    four = code[2]
    eight = code[-1]

    top = [x for x in seven if x not in one][0]

    top_left_and_middle = [x for x in four if x not in one]

    # 9
    for number in code[6:9]:
        for letter in four:
            if letter not in number:
                break
        else:
            nine = number

    # bottom_left
    for letter in eight:
        if letter not in nine:
            bottom_left = letter
            break

    # 2
    for number in code[3:6]:
        if bottom_left in number:
            two = number
            break

    # bottom
    for letter in two:
        if letter not in four:
            if letter not in [top, bottom_left]:
                bottom = letter
                break

    # middle
    for letter in two:
        if letter not in [top, bottom_left, bottom]:
            if letter not in one:
                middle = letter
                break

    # top_right
    for letter in two:
        if letter not in [top, middle, bottom_left, bottom]:
            top_right = letter
            break

    # bottom_right
    for letter in one:
        if letter != top_right:
            bottom_right = letter
            break

    # top_left
    for letter in four:
        if letter not in [top_right, middle, bottom_right]:
            top_left = letter
            break

    # 3 and 5
    for number in code[3:6]:
        if top_left not in number and bottom_left not in number:
            three = number
            continue
        if top_right not in number and bottom_left not in number:
            five = number
            continue

    # 0 and 6
    for number in code[6:9]:
        if middle not in number:
            zero = number
            continue
        if top_right not in number:
            six = number

    digits = [zero, one, two, three, four, five, six, seven, eight, nine]

    digits = [''.join(sorted(x)) for x in digits]

    out = ""

    for number in output.split(' '):
        out += str(digits.index(''.join(sorted(number))))

    summed_output += int(out)

print("Part 2: " + str(summed_output))

print("Time:", time() - t1)
