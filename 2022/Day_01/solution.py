from time import perf_counter

import pytest


def format_time(func):
    def wrapper(*args, **kwargs):
        t1 = perf_counter()
        func(*args, **kwargs)
        t2 = perf_counter()
        time_delta = t2 - t1
        print("Time: {:.3f} seconds".format(time_delta))
    return wrapper()


def compute(data):
    elves = data.split("\n\n")
    return max(sum(map(int, elf.split())) for elf in elves)


def compute2(data):
    data = data.split("\n\n")
    elves = [sum(map(int, elf.split())) for elf in data]
    return sum(sorted(elves, reverse=True)[:3])


def main():
    print("Part 1: {}".format(compute(open("2022/Day_01/input.txt").read())))
    print("Part 2: {}".format(compute2(open("2022/Day_01/input.txt").read())))


@pytest.mark.parametrize("input_, expected", [
    ("""1000
2000
3000

4000

5000
6000

7000
8000
9000

10000""", 24000)])
def test(input_, expected):
    assert compute(input_) == expected


@pytest.mark.parametrize("input_, expected", [
    ("""1000
2000
3000

4000

5000
6000

7000
8000
9000

10000""", 45000)])
def test2(input_, expected):
    assert compute2(input_) == expected


if __name__ == "__main__":
    format_time(main)
