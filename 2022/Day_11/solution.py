import pytest
import re
from collections import defaultdict

from time import perf_counter


def format_time(func):
    def wrapper(*args, **kwargs):
        t1 = perf_counter()
        func(*args, **kwargs)
        t2 = perf_counter()
        time_delta = t2 - t1
        print("Time: {:.3f} seconds".format(time_delta))

    return wrapper()


def parse_data(data):
    monkeys_raw = data.split("\n\n")
    monkeys = defaultdict(dict)
    for monkey_raw in monkeys_raw:
        lines = monkey_raw.splitlines()
        monkey_num = int(re.findall("\\d+", lines[0])[0])
        monkeys[monkey_num]["items"] = [
            int(x) for x in re.findall("\\d+", lines[1])
        ]
        monkeys[monkey_num]["operation"] = re.findall(
            "(\\+|\\*) (\\d+|old)", lines[2]
        )[0]
        monkeys[monkey_num]["test"] = re.findall("\\d+", lines[3])[0]
        monkeys[monkey_num]["if_true"] = int(re.findall("\\d+", lines[4])[0])
        monkeys[monkey_num]["if_false"] = int(re.findall("\\d+", lines[5])[0])
        monkeys[monkey_num]["inspect_count"] = 0

    return monkeys


def compute1(data):
    monkeys = parse_data(data)
    max_rounds = 20
    for i in range(max_rounds):
        for monkey_num, monkey in monkeys.items():
            while monkey["items"]:
                item = monkey["items"][0]
                monkey["inspect_count"] += 1
                # Operation
                if monkey["operation"][0] == "+":
                    if monkey["operation"][1] == "old":
                        item += item
                    else:
                        item += int(monkey["operation"][1])
                elif monkey["operation"][0] == "*":
                    if monkey["operation"][1] == "old":
                        item *= item
                    else:
                        item *= int(monkey["operation"][1])

                # Divide by 3
                item //= 3

                # Test
                if item % int(monkey["test"]) == 0:
                    monkeys[monkey["if_true"]]["items"].append(item)
                else:
                    monkeys[monkey["if_false"]]["items"].append(item)
                del monkey["items"][0]

    inspects = []
    for monkey in monkeys.values():
        inspects.append(monkey["inspect_count"])
    total_inspect_count = sorted(inspects)[-1] * sorted(inspects)[-2]

    return total_inspect_count


def compute2(data):
    monkeys = parse_data(data)
    mod = 1
    for monkey in monkeys.values():
        mod *= int(monkey["test"])
    max_rounds = 10000
    for i in range(max_rounds):
        for monkey_num, monkey in monkeys.items():
            while monkey["items"]:
                item = monkey["items"][0]
                monkey["inspect_count"] += 1
                # Operation
                if monkey["operation"][0] == "+":
                    if monkey["operation"][1] == "old":
                        item += item
                    else:
                        item += int(monkey["operation"][1])
                elif monkey["operation"][0] == "*":
                    if monkey["operation"][1] == "old":
                        item *= item
                    else:
                        item *= int(monkey["operation"][1])

                item %= mod
                # Test
                if item % int(monkey["test"]) == 0:
                    monkeys[monkey["if_true"]]["items"].append(item)
                else:
                    monkeys[monkey["if_false"]]["items"].append(item)
                del monkey["items"][0]

    inspects = []
    for monkey in monkeys.values():
        inspects.append(monkey["inspect_count"])
    total_inspect_count = sorted(inspects)[-1] * sorted(inspects)[-2]

    return total_inspect_count


def main():
    with open("2022/Day_11/input.txt") as f:
        data = f.read()
    answer = compute1(data)
    print(answer)
    answer = compute2(data)
    print(answer)


@pytest.mark.parametrize(
    "input_, expected",
    [
        (
            """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1""",
            10605,
        ),
    ],
)
def test1(input_, expected):
    assert compute1(input_) == expected


@pytest.mark.parametrize(
    "input_, expected",
    [
        (
            """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1""",
            2713310158,
        ),
    ],
)
def test2(input_, expected):
    assert compute2(input_) == expected


if __name__ == "__main__":
    format_time(main)
