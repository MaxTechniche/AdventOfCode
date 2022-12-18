import pytest
import re
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


def compute1(data, row):
    s_b = data.splitlines()
    sensors = dict()
    beacons = set()
    row_spots = set()
    for line in s_b:
        s_x, s_y, b_x, b_y = map(int, re.findall(r"-?\d+", line))
        sensors[(s_x, s_y)] = (b_x, b_y)
        beacons.add((b_x, b_y))
        dif = abs(s_y - b_y) - abs(s_y - row)
        tfs = abs(s_x - b_x) * 2 + 1 + (dif * 2)
        if tfs > 0:
            for i in range((tfs-1)//2 + 1):
                row_spots.add(s_x - i)
                row_spots.add(s_x + i)
            # row_spots.add(s_x)
        for b in beacons:
            if b[1] == row:
                if b[0] in row_spots:
                    row_spots.remove(b[0])
                
    # print(row_spots)
    print()
    print(len(row_spots))
    
    return len(row_spots)
    
    # print()
    # print("SENSORS")
    # print(*sensors.items(), sep="\n")
    # print()
    # print("BEACONS")
    # print(*beacons, sep="\n")


def compute2(data, limit=21):
    s_b = [list(map(int, re.findall(r"-?\d+", line))) for line in data.splitlines()]
    print(s_b)
    for row in range(limit):
        row_range = list()
        for line in s_b:
            s_x, s_y, b_x, b_y = line

            dif = abs(s_y - b_y) - abs(s_y - row)
            tfs = abs(s_x - b_x) * 2 + 1 + (dif * 2)
            if tfs > 0:
                row_range.append(range(s_x - (tfs-1)//2, s_x + (tfs-1)//2))

        row_range.sort(key=lambda x: x.start)
        ranges = [row_range[0]]
        for i in row_range[1:]:
            rc = ranges[-1]
            if i.start >= rc.start and i.start - 1 <= rc.stop:
                ranges[-1] = range(min(i.start, rc.start), max(i.stop, rc.stop))
            else:
                ranges.append(i)
        if len(ranges) == 2:
            print()
            x = ranges[0].stop + 1
            print(ranges)
            print(x, row)
            return x * 4000000 + row


def main():
    with open("2022/Day_15/input.txt") as f:
        data = f.read()
    answer = compute1(data, 2000000)  # was 10
    print(answer)
    answer = compute2(data, 4000000)
    print(answer)


@pytest.mark.parametrize("input_, row, expected", [
    ("""Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3""", 10, 26),
    ])
def test1(input_, row, expected):
    assert compute1(input_, row) == expected


@pytest.mark.parametrize("input_, expected", [
    ("""Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3""", 56000011),
    ])
def test2(input_, expected):
    assert compute2(input_) == expected


if __name__ == "__main__":
    format_time(main)
