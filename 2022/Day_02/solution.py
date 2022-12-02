import pytest

from time import perf_counter

points_1 = {
    "W": 6,
    "D": 3,
    "L": 0,
    "X": 1,  # Rock
    "Y": 2,  # Paper
    "Z": 3,  # Scissors
}


poss_1 = {
    "A X": "D",
    "A Y": "W",
    "A Z": "L",
    "B X": "L",
    "B Y": "D",
    "B Z": "W",
    "C X": "W",
    "C Y": "L",
    "C Z": "D",
}

points_2 = {
    "W": 6,
    "D": 3,
    "L": 0,
    "X": 1,  # Rock
    "Y": 2,  # Paper
    "Z": 3,  # Scissors
}

poss_2 = {
    "A X": ("L", "Z"),
    "A Y": ("D", "X"),
    "A Z": ("W", "Y"),
    "B X": ("L", "X"),
    "B Y": ("D", "Y"),
    "B Z": ("W", "Z"),
    "C X": ("L", "Y"),
    "C Y": ("D", "Z"),
    "C Z": ("W", "X"),
}




def format_time(func):
    def wrapper(*args, **kwargs):
        t1 = perf_counter()
        func(*args, **kwargs)
        t2 = perf_counter()
        time_delta = t2 - t1
        print("Time: {:.3f} seconds".format(time_delta))
    return wrapper()


def compute1(data):
    total = 0
    for line in data.splitlines():
        opponent, us = line.split()
        total += points_1[us]
        total += points_1[poss_1[line.strip()]]
    return total


def compute2(data):
    total = 0
    for line in data.splitlines():
        opponent, us = line.split()
        total += points_2[poss_2[line][0]]
        total += points_2[poss_2[line][1]]
    return total


def main():
    with open("2022/Day_02/input.txt") as f:
        data = f.read()
    answer = compute1(data)
    print("Part 1:", answer)
    answer = compute2(data)
    print("Part 2:", answer)


@pytest.mark.parametrize("input_, expected", [
    ("""A Y
B X
C Z""", 15),
    ])
def test1(input_, expected):
    assert compute1(input_) == expected


@pytest.mark.parametrize("input_, expected", [
    ("""A Y
B X
C Z""", 12),
    ])
def test2(input_, expected):
    assert compute2(input_) == expected

if __name__ == "__main__":
    format_time(main)
