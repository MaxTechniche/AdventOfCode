import pytest

from time import perf_counter


def format_time(func):
    def wrapper(*args, **kwargs):
        t1 = perf_counter()
        func(*args, **kwargs)
        t2 = perf_counter()
        time_delta = t2 - t1
        if time_delta * 1000 < 1:
            print(f"{time_delta * 1000000:.3f} μs")
        elif time_delta < 1:
            print(f"{time_delta * 1000:.3f} ms")
        else:
            print(f"{time_delta:.3f} s")
    return wrapper()


def compute1(data):
    total = 0
    pairs = data.split("\n")
    for pair in pairs:
        sections = pair.split(",")
        sect1 = sections[0].split("-")
        sect2 = sections[1].split("-")
        if (int(sect1[0]) >= int(sect2[0]) and int(sect1[1]) <= int(sect2[1])) or (int(sect2[0]) >= int(sect1[0]) and int(sect2[1]) <= int(sect1[1])):
            total += 1
    return total


def compute2(data):
    total = 0
    pairs = data.split("\n")
    for pair in pairs:
        sections = pair.split(",")
        sect1 = sections[0].split("-")
        sect2 = sections[1].split("-")
        if (int(sect1[0]) in range(int(sect2[0]), int(sect2[1])+1) or int(sect1[1]) in range(int(sect2[0]), int(sect2[1])+1)) or (int(sect2[0]) in range(int(sect1[0]), int(sect1[1])+1) or int(sect2[1]) in range(int(sect1[0]), int(sect1[1])+1)):
            total += 1
    return total


def main():
    with open("2022/Day_04/input.txt") as f:
        data = f.read()
    answer = compute1(data)
    print(answer)
    answer = compute2(data)
    print(answer)


@pytest.mark.parametrize("input_, expected", [
    ("""2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8""", 2),
    ])
def test1(input_, expected):
    assert compute1(input_) == expected


@pytest.mark.parametrize("input_, expected", [
    ("""2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8""", 4),
    ])
def test2(input_, expected):
    assert compute2(input_) == expected


if __name__ == "__main__":
    format_time(main)
