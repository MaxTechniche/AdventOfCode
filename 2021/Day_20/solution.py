from time import time
from pprint import pprint


def get_binary(pos, image, char='#'):
    x, y = pos
    bin_string = ''
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if x+i < 0 or y+j < 0:
                if image[x][y] == '#':
                    bin_string += '1'
                else:
                    bin_string += '0'
            elif x+i >= len(image) or y+j >= len(image[0]):
                if image[x][y] == '#':
                    bin_string += '1'
                else:
                    bin_string += '0'
            else:
                if image[x+i][y+j] == '#':
                    bin_string += '1'
                else:
                    bin_string += '0'

    return int(bin_string, 2)


def buffer(image, t, code):
    char = '.'
    if code[0] == '#' and code[-1] == '.':
        if t % 2 == 1:
            char = '#'

    buff = char * (len(image[0]))

    image = [buff] + image + [buff]

    for i in range(len(image)):
        image[i] = char + image[i] + char

    return image


def enhance_image(image, code):
    next_image = []

    for x in range(len(image)):
        row = ''
        for y in range(len(image[x])):
            row += code[get_binary((x, y), image)]
        next_image.append(row)

    return next_image


def get_lit(image):
    count = 0
    for row in image:
        count += row.count('#')

    return count


def main():
    t1 = time()

    with open("2021/Day_20/input") as f:
        lines = f.read().splitlines()
    code = lines[0]
    image = lines[2:]

    for t in range(50):
        image = buffer(image, t, code)
        image = enhance_image(image, code)

    pprint(image)
    print(get_lit(image))

    print("Time:", time() - t1)


main()
