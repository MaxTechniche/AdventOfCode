import pytest

from time import perf_counter


def format_time(func):
    def wrapper(*args, **kwargs):
        t1 = perf_counter()
        func(*args, **kwargs)
        t2 = perf_counter()
        time_delta = t2 - t1
        print("Time: {:.3f} seconds".format(time_delta))
    return wrapper()


def compute1(data):
    pass


def compute2(data):
    pass


def main():
    with open("2022/Day_09/input.txt") as f:
        data = f.read()
    answer = compute1(data)
    print(answer)


@pytest.mark.parametrize("input_, expected", [
    ("", 0),
    ])
def test1(input_, expected):
    assert compute1(input_) == expected


@pytest.mark.parametrize("input_, expected", [
    ("", 0),
    ])
def test2(input_, expected):
    assert compute2(input_) == expected


if __name__ == "__main__":
    format_time(main)
