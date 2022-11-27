from time import time
from copy import deepcopy


def display(m):
    for row in m:
        print(''.join(row))
    print('')


def east_move(m):
    c = deepcopy(m)
    for row in range(len(m)):
        for column in range(len(m[row])):
            if m[row][column] == '>':
                if column == len(m[row])-1:
                    if m[row][0] == '.':
                        c[row][0] = '>'
                        c[row][column] = '.'
                else:
                    if m[row][column+1] == '.':
                        c[row][column+1] = '>'
                        c[row][column] = '.'
    return c


def south_move(m):
    c = deepcopy(m)
    for row in range(len(m)):
        for column in range(len(m[row])):
            if m[row][column] == 'v':

                if row == len(m)-1:
                    if m[0][column] == '.':
                        c[0][column] = 'v'
                        c[row][column] = '.'
                else:
                    if m[row+1][column] == '.':
                        c[row+1][column] = 'v'
                        c[row][column] = '.'
    return c


def main():
    t1 = time()

    with open("2021/Day_25/input") as f:
        m = [list(line) for line in f.read().splitlines()]

    c = deepcopy(m)
    step = 0
    while True:
        step += 1
        print(step)
        m = deepcopy(c)
        c = east_move(m)
        c = south_move(c)
        if c == m:
            break

    print(step)

    print("Time:", time() - t1)


main()
