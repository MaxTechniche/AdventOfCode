import pytest

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


def compute1(data):
    X = 1
    current_cycle = 0
    cycle_strengths = []
    cycle_checks = [20]
    cycle_checks.extend(range(60, 221, 40))

    executions = data.splitlines()
    for execution in executions:
        if execution == "noop":
            current_cycle += 1
            if current_cycle in cycle_checks:
                cycle_strengths.append(current_cycle * X)
        elif execution.startswith("addx"):
            V = int(execution.split(" ")[1])
            for c in (1, 2):
                current_cycle += 1
                if current_cycle in cycle_checks:
                    cycle_strengths.append(current_cycle * X)
                if c == 2:
                    X += V
    return sum(cycle_strengths)


def compute2(data):
    sprite_pos = 1
    current_cycle = 0
    CRT = [["."] * 40 for _ in range(6)]
    current_row = 0

    executions = data.splitlines()
    for execution in executions:
        if execution == "noop":
            if current_cycle % 40 in range(sprite_pos - 1, sprite_pos + 2):
                CRT[current_row][current_cycle % 40] = "#"
            current_cycle += 1
            if current_cycle % 40 == 0:
                current_row += 1
        elif execution.startswith("addx"):
            V = int(execution.split(" ")[1])
            for c in (1, 2):
                if current_cycle % 40 in range(sprite_pos - 1, sprite_pos + 2):
                    CRT[current_row][current_cycle % 40] = "#"
                current_cycle += 1
                if current_cycle % 40 == 0:
                    current_row += 1
                if c == 2:
                    sprite_pos += V


    # print("\n".join([" ".join(row) for row in CRT]))
    return "\n".join(["".join(row) for row in CRT])
    # return "\n".join(CRT)


def main():
    with open("2022/Day_10/input.txt") as f:
        data = f.read()
    answer = compute1(data)
    print(answer)
    compute2(data)


@pytest.mark.parametrize("input_, expected", [
    ("""addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop""", 13140),
    ])
def test1(input_, expected):
    assert compute1(input_) == expected


@pytest.mark.parametrize("input_, expected", [
    ("""addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop""", """##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######....."""),
    ])
def test2(input_, expected):
    assert compute2(input_) == expected


if __name__ == "__main__":
    format_time(main)
