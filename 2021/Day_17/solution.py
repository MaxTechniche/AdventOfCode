from time import time


def main():
    t1 = time()

    with open("2021/Day_17/input") as f:
        x, y = f.read().split(', ')
        x = x.split(': ')[1]
        xmin, xmax = x.split('..')
        ymin, ymax = y.split('..')
        xmin = int(xmin[2:])
        ymin = int(ymin[2:])
        xmax = int(xmax)
        ymax = int(ymax)

    print(xmin, xmax, ymin, ymax)

    x_values = []
    for x_start in range(1, xmax+1):
        xv = x_start
        x_pos = 0
        steps = 0
        while x_pos < xmin:
            steps += 1
            if xv <= 0:
                break
            x_pos += xv
            xv -= 1
        else:
            if xmin <= x_pos <= xmax:
                x_values.append(x_start)

    y_values = []
    for y_start in range(ymin, abs(ymin)+1):
        yv = y_start
        y_pos = 0
        steps = 0
        while y_pos > ymax:
            y_pos += yv
            yv -= 1
        else:
            if ymin <= y_pos <= ymax:
                y_values.append(y_start)

    successes = []
    for y_start in y_values:
        for x_start in x_values:
            xv = x_start
            yv = y_start
            x_pos = 0
            y_pos = 0
            max_y = 0
            while True:
                max_y = max(max_y, y_pos)
                if xmin <= x_pos <= xmax and ymin <= y_pos <= ymax:
                    successes.append(max_y)
                    break
                if y_pos < ymin or x_pos > xmax:
                    break
                x_pos += xv
                xv -= 1
                xv = max(xv, 0)
                y_pos += yv
                yv -= 1

    print(max(successes))
    print(len(successes))

    print("Time:", time() - t1)


main()
