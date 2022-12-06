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


def compute(data, num_unique=4):
    for i, character in enumerate(data):
        if len(set(data[i:i+num_unique])) == num_unique:
            return i + num_unique


def main():
    with open("2022/Day_06/input.txt") as f:
        data = f.read()
    answer = compute(data, 4)
    print(answer)
    answer = compute(data, 14)
    print(answer)


@pytest.mark.parametrize("data, unique, expected", [
    ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 4, 7),
    ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 14, 19),
    ("bvwbjplbgvbhsrlpgdmjqwftvncz", 4, 5),
    ("bvwbjplbgvbhsrlpgdmjqwftvncz", 14, 23),
    ("nppdvjthqldpwncqszvftbrmjlhg", 4, 6),
    ("nppdvjthqldpwncqszvftbrmjlhg", 14, 23),
    ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 4, 10),
    ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 14, 29),
    ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 4, 11),
    ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 14, 26),
    ])
def test1(data, unique, expected):
    assert compute(data, unique) == expected


if __name__ == "__main__":
    format_time(main)
