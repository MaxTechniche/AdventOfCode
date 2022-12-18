import pytest
import ast
from itertools import zip_longest

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


def solve(left, right):
    # print(left, right)
    compare = None
    if isinstance(left, int) and isinstance(right, int):
        if left > right:
            return False
        if left < right:
            return True

    elif isinstance(left, list) and isinstance(right, list):
        for a, b in zip_longest(left, right):
            if a is None:
                return True
            elif b is None:
                return False

            compare = solve(a, b)
            if compare is True:
                return True
            if compare is False:
                return False
    elif isinstance(left, int) and isinstance(right, list):
        compare = solve([left], right)

    elif isinstance(right, int) and isinstance(left, list):
        compare = solve(left, [right])

    if compare is False:
        return False
    elif compare is True:
        return True
    return None


def compute1(data):
    pairs = data.split("\n\n")
    total = 0
    for i, pair in enumerate(pairs, 1):
        left, right = pair.strip().split("\n")
        left = ast.literal_eval(left)
        right = ast.literal_eval(right)
        if solve(left, right):
            # print(i, "good")
            total += i
        else:
            pass
            # print(i, "bad")
        # print()
    return total


def compute2(data):
    pairs = data.replace("\n\n", "\n").split("\n")
    pairs.append("[[2]]")
    pairs.append("[[6]]")
    pairs = [ast.literal_eval(pair) for pair in pairs]
    sorted_pairs = [pairs[0]]
    for pair in pairs[1:]:
        for i, sorted_pair in enumerate(sorted_pairs):
            if solve(pair, sorted_pair):
                sorted_pairs.insert(i, pair)
                break
        else:
            sorted_pairs.append(pair)
    # print(sorted_pairs, sep="\n")
    pos = 1
    for i, pair in enumerate(sorted_pairs, 1):
        if pair == [[2]] or pair == [[6]]:
            pos *= i
            
    return pos



def main():
    with open("2022/Day_13/input.txt") as f:
        data = f.read()
    answer = compute1(data)
    print(answer)
    answer = compute2(data)
    print(answer)


@pytest.mark.parametrize("input_, expected", [
    ("""[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]""", 13),
    ])
def test1(input_, expected):
    assert compute1(input_) == expected


@pytest.mark.parametrize("input_, expected", [
    ("""[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]""", 140),
    ])
def test2(input_, expected):
    assert compute2(input_) == expected


if __name__ == "__main__":
    format_time(main)
