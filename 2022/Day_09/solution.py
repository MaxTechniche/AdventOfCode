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


directions = {
    "U": (0, -1),
    "D": (0, 1),
    "R": (1, 0),
    "L": (-1, 0),
}


# def visualize(head, tails, grid_size)


def within_one(hx, hy, tx, ty):
    if abs(hx - tx) <= 1 and abs(hy - ty) <= 1:
        return True
    return False


def compute1(data, num_tails=1):
    tail = [0, 0]
    tail_visited = set()
    tail_visited.add(tuple(tail))
    head = [0, 0]

    data = data.splitlines()
    for line in data:
        direction, distance = line.strip().split()
        direction = directions[direction]
        for x in range(int(distance)):
            head[0] += direction[0]
            head[1] += direction[1]
            if within_one(*head, *tail):
                continue
            tail[0] += direction[0]
            tail[1] += direction[1]
            if direction[0] != 0:
                tail[1] = head[1]
            elif direction[1] != 0:
                tail[0] = head[0]
            tail_visited.add(tuple(tail))

    return len(tail_visited)


def compute2(data, num_tails=9):
    head = [0, 0]
    tails = [list(head) for _ in range(num_tails)]
    tail_visited = set()
    tail_visited.add(tuple(head))

    data = data.splitlines()
    for line in data:
        direction, distance = line.strip().split()
        direction = directions[direction]
        for x in range(int(distance)):
            head[0] += direction[0]
            head[1] += direction[1]
            for tail in range(num_tails):
                if tail == 0:
                    if within_one(*head, *tails[tail]):
                        continue
                    tails[tail][0] += direction[0]
                    tails[tail][1] += direction[1]
                    if direction[0] != 0:
                        tails[tail][1] = head[1]
                    elif direction[1] != 0:
                        tails[tail][0] = head[0]
                else:
                    if within_one(*tails[tail-1], *tails[tail]):
                        continue

                    if tails[tail-1][0] < tails[tail][0]:
                        tails[tail][0] -= 1
                    elif tails[tail-1][0] > tails[tail][0]:
                        tails[tail][0] += 1

                    if tails[tail-1][1] < tails[tail][1]:
                        tails[tail][1] -= 1
                    elif tails[tail-1][1] > tails[tail][1]:
                        tails[tail][1] += 1
            tail_visited.add(tuple(tails[-1]))

    return len(tail_visited)


def main():
    with open("2022/Day_09/input.txt") as f:
        data = f.read()
    answer = compute1(data)
    print(answer)
    answer = compute2(data)
    print(answer)


@pytest.mark.parametrize("input_, expected", [
    ("""R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2""", 13),
    ])
def test1(input_, expected):
    assert compute1(input_) == expected


@pytest.mark.parametrize("input_, expected", [
    ("""R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20""", 36),
    ])
def test2(input_, expected):
    assert compute2(input_) == expected


if __name__ == "__main__":
    format_time(main)
