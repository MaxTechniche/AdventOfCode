from time import time


def main():
    t1 = time()

    with open("2021/Day_13/input") as f:
        lines = f.read().split('\n\n')
        dots = set(tuple(map(int, line.split(',')))
                   for line in lines[0].splitlines())
        folds = lines[1].splitlines()

    next_dots = set()
    for total_folds, fold in enumerate(folds, 1):
        fold = fold.split(' ')[-1].split('=')
        axis, location = fold
        axis = 0 if axis == 'x' else 1
        location = int(location)

        next_dots.clear()

        for dot in dots:
            xy = [dot[0], dot[1]]
            if dot[axis] > location:
                xy[axis] = xy[axis] - 2 * (xy[axis] - location)
            next_dots.add((xy[0], xy[1]))
        dots = next_dots.copy()
        print("After fold " + str(total_folds) + ': ' + str(len(next_dots)))

    xs = []
    ys = []

    for dot in dots:
        xs.append(dot[0])
        ys.append(dot[1])

    max_x = max(xs)
    max_y = max(ys)

    grid = [['.' for x in range(max_x+1)] for y in range(max_y+1)]

    for dot in dots:
        grid[dot[1]][dot[0]] = '#'

    for row in grid:
        print(' '.join(row))
        pass

    print("Time:", time() - t1)


main()
