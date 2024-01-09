import pytest
from itertools import cycle
from time import perf_counter

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


def direction(symbol, x, y, max_x, max_y):
    if symbol == ">":
        if x + 1 < max_x:
            return (x + 1, y)
        else:
            return (0, y)
        
    elif symbol == "<":
        if x - 1 >= 0:
            return (x - 1, y)
        else:
            return (max_x - 1, y)
        
    elif symbol == "^":
        if y - 1 >= 0:
            return (x, y - 1)
        else:
            return (x, max_y - 1)
        
    elif symbol == "v":
        if y + 1 < max_y:
            return (x, y + 1)
        else:
            return (x, 0)


def compute1(data):
    data = [list(line.strip().strip("#")) for line in data.splitlines()[1:-1]]
    blizzard_dirs = {
        ">": [],
        "<": [],
        "^": [],
        "v": [],
    }
    waits = [[[] for _ in range(len(data[0]))] for _ in range(len(data))]
    for j, row in enumerate(data):
        for i, col in enumerate(row):
            if col != ".":
                blizzard_dirs[col].append((i, j))
    counts = [[0 for _ in range(len(data[0]))] for _ in range(len(data))]
    m = 0
    while m < 100000:
        print(m)
        count_copy = [row[:] for row in counts]
        for d, blizzards in blizzard_dirs.items():
            for i, blizzard in enumerate(blizzards):
                next_pos = direction(d, blizzard[0], blizzard[1], len(data[0]), len(data))
                counts[blizzard[1]][blizzard[0]] += 1
                blizzards[i] = list(next_pos)
        for j, row in enumerate(counts):
            for i, col in enumerate(row):
                if col == count_copy[j][i]:
                    waits[j][i].append(m)
        m += 1
    


def compute2(data):
    pass


def main():
    with open("2022/Day_25/input.txt") as f:
        data = f.read()
    answer = compute1(data)
    print(answer)


@pytest.mark.parametrize(
    "input_, expected",
    [
        ("""#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#""", 18),
    ],
)
def test1(input_, expected):
    assert compute1(input_) == expected


@pytest.mark.parametrize(
    "input_, expected",
    [
        ("""#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#""", 0),
    ],
)
@pytest.mark.skip
def test2(input_, expected):
    assert compute2(input_) == expected


if __name__ == "__main__":
    format_time(main)
