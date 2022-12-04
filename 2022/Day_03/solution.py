import pytest

from time import perf_counter

from string import ascii_letters

priorities = {v: i for i, v in enumerate(ascii_letters, 1)}


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
    rucksacks = data.split("\n")
    total_priority = 0
    for rucksack in rucksacks:
        ruck_len = len(rucksack)
        left, right = rucksack[: ruck_len // 2], rucksack[ruck_len // 2:]
        for letter in left:
            if letter in right:
                total_priority += priorities[letter]
                break
    return total_priority


def compute2(data):
    rucksacks = data.split("\n")
    total_priority = 0
    for r in range(0, len(rucksacks), 3):
        rucksack_group = rucksacks[r:r + 3]
        for letter in rucksack_group[0]:
            if letter in rucksack_group[1] and letter in rucksack_group[2]:
                total_priority += priorities[letter]
                break
    return total_priority


def main():
    with open("2022/Day_03/input.txt") as f:
        data = f.read()
    answer = compute1(data)
    print("Part 1:", answer)
    answer = compute2(data)
    print("Part 2:", answer)


@pytest.mark.parametrize(
    "input_, expected",
    [
        (
            """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw""",
            157,
        ),
    ],
)
def test1(input_, expected):
    assert compute1(input_) == expected


@pytest.mark.parametrize(
    "input_, expected",
    [
        (
            """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw""",
            70,
        ),
    ],
)
def test2(input_, expected):
    assert compute2(input_) == expected


if __name__ == "__main__":
    format_time(main)
