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
    stacks_raw, commands = data.split("\n\n")

    stacks = dict()
    for row in stacks_raw.splitlines():
        for i in range(1, len(row), 4):
            val = int(i) // 4 + 1
            try:
                if row[i] == " ":
                    continue
                int(row[i])
                continue
            except ValueError:
                pass
            if val not in stacks:
                stacks[val] = [row[i]]
            else:
                stacks[val].insert(0, row[i])

    for command in commands.splitlines():
        move, f, t = map(int, command.split()[1::2])
        for m in range(move):
            stacks[t].append(stacks[f].pop())

    tops = ""
    for i in range(1, len(stacks) + 1):
        tops += stacks[i].pop()
    return tops


def compute2(data):
    stacks_raw, commands = data.split("\n\n")
    stacks = dict()
    for row in stacks_raw.splitlines():
        for i in range(1, len(row), 4):
            val = int(i) // 4 + 1
            try:
                if row[i] == " ":
                    continue
                int(row[i])
                continue
            except ValueError:
                pass
            if val not in stacks:
                stacks[val] = [row[i]]
            else:
                stacks[val].insert(0, row[i])

    for command in commands.splitlines():
        move, f, t = map(int, command.split()[1::2])
        stacks[t].extend(stacks[f][-move:])
        stacks[f] = stacks[f][:-move]

    tops = ""
    for i in range(1, len(stacks) + 1):
        tops += stacks[i].pop()
    return tops


def main():
    with open("2022/Day_05/input.txt") as f:
        data = f.read()
    answer = compute1(data)
    print(answer)
    answer = compute2(data)
    print(answer)


@pytest.mark.parametrize(
    "input_, expected",
    [
        (
            """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2""",
            "CMZ",
        ),
    ],
)
def test1(input_, expected):
    assert compute1(input_) == expected


@pytest.mark.parametrize(
    "input_, expected",
    [
        (
            """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2""",
            "MCD",
        ),
    ],
)
def test2(input_, expected):
    assert compute2(input_) == expected


if __name__ == "__main__":
    format_time(main)
