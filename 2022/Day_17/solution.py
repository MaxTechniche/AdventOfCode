import pytest
from itertools import cycle
from time import perf_counter
import numpy as np

def format_time(func):
    def wrapper(*args, **kwargs):
        t1 = perf_counter()
        func(*args, **kwargs)
        t2 = perf_counter()
        time_delta = t2 - t1
        if time_delta * 1000 < 1:
            print(str(time_delta * 1000000)[:6], "μs")
        elif time_delta < 1:
            print(str(time_delta * 1000)[:6], "ms")
        else:
            print(str(time_delta)[:6], "s")

    return wrapper()


rock_types = [
    """####""",
    """.#.
###
.#.""",
    """..#
..#
###""",
    """#
#
#
#""",
    """##
##""",
]

rocks = []
for rock in rock_types:
    rock = rock.split("\n")
    roc = []
    for r in rock:
        roc.append(list(r))
    rocks.append(np.array(roc))
rock_types = rocks
print(rock_types)


def shift(x, y, d, rock, placed, direction=None):
    if x + rock.shape[1] > 7:
        if d == 1:
            return False
    elif x == 0:
        if d == -1:
            return False
    for i, row in enumerate(rock):
        for j, col in enumerate(row):
            if col == "#":
                try:
                    if placed[y + i][x + j + d] == "#":
                        return False
                except IndexError:
                    return False
    return True


def drop(x, y, rock, placed):
    if y == 0:
        return False
    for i, row in enumerate(rock):
        for j, col in enumerate(row):
            if col == "#":
                try:
                    if placed[y + i + 1][x + j] == "#":
                        return False
                except IndexError:
                    return False
    return True


def place(x, y, rock, placed):
    for i, row in enumerate(rock):
        for j, col in enumerate(row):
            if col == "#":
                placed[y + i][x + j] = "#"
    
    if placed.shape[0] < y + rock.shape[0] + 1:
        p = np.array([["." for x in range(7)] for y in range(4)])
        placed = np.concatenate((placed, p), axis=0)
    return placed


def compute1(data):
    direct = lambda x: 1 if x == ">" else -1
    placed = np.array([["." for x in range(7)] for y in range(10)])
    rocks = cycle(rock_types)
    gas_dir = cycle(data.strip())
    top = 0
    for fallen in range(2022):
        rock = next(rocks)
        y = top + 4
        x = 2
        while True:
            temp = placed.copy()
            # print(temp[y:y+rock.shape[0], x:x+rock.shape[1]])
            print(temp.shape)
            print(rock.shape, temp[y:y+rock.shape[0], x:x+rock.shape[1]].shape)
            temp[y:y+rock.shape[0], x:x+rock.shape[1]] = rock
            print(temp)
            
            d = direct(next(gas_dir))
            if shift(x, y, d, rock, placed):
                x += d
            if not drop(x, y, rock, placed):
                placed = place(x, y, rock, placed)
                top = max(top, y)
                break
            y -= 1


def compute2(data):
    pass


def main():
    with open("2022/Day_17/input.txt") as f:
        data = f.read()
    answer = compute1(data)
    print(answer)


@pytest.mark.parametrize(
    "input_, expected",
    [
        (">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>", 3068),
    ],
)
def test1(input_, expected):
    assert compute1(input_) == expected


@pytest.mark.parametrize(
    "input_, expected",
    [
        (">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>", 0),
    ],
)
@pytest.mark.skip
def test2(input_, expected):
    assert compute2(input_) == expected


if __name__ == "__main__":
    format_time(main)
