import pytest
from pprint import pprint
from time import perf_counter
from math import prod


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


class Tree:
    def __init__(self, height, x, y):
        self.height = height
        self.x = x
        self.y = y
        self.highest_n = self.height
        self.highest_e = self.height
        self.highest_s = self.height
        self.highest_w = self.height
        self.visible = False

    def __repr__(self):
        return str(self.height)


def directions(x, y):
    return [
        (x, y - 1),
        (x + 1, y),
        (x, y + 1),
        (x - 1, y),
        ]


def direction_absolutes():
    return [
        (0, -1),
        (1, 0),
        (0, 1),
        (-1, 0),
        ]


def compute1(data):
    grid = []
    for y, line in enumerate(data.splitlines()):
        grid.append([])
        for x, char in enumerate(line):
            grid[y].append(Tree(char, x, y))


    for y in range(len(grid)):
        for x in range(len(grid[y])):
            tree = grid[y][x]
            if x - 1 >= 0:
                tl = grid[y][x - 1]
                if tl.highest_w >= tree.height:
                    tree.highest_w = tl.highest_w
                else:
                    tree.visible = True
            else:
                tree.visible = True

            if y - 1 >= 0:
                tu = grid[y - 1][x]
                if tu.highest_n >= tree.height:
                    tree.highest_n = tu.highest_n
                else:
                    tree.visible = True
            else:
                tree.visible = True

    for y in range(len(grid) - 1, -1, -1):
        for x in range(len(grid[y]) - 1, -1, -1):
            tree = grid[y][x]
            if x + 1 < len(grid[y]):
                tr = grid[y][x + 1]
                if tr.highest_e >= tree.height:
                    tree.highest_e = tr.highest_e
                else:
                    tree.visible = True
            else:
                tree.visible = True

            if y + 1 < len(grid):
                td = grid[y + 1][x]
                if td.highest_s >= tree.height:
                    tree.highest_s = td.highest_s
                else:
                    tree.visible = True
            else:
                tree.visible = True

    total = 0
    for row in grid:
        for tree in row:
            if tree.visible:
                total += 1


    return total


def compute2(data):
    grid = []
    for y, line in enumerate(data.split("\n")):
        grid.append([])
        for x, char in enumerate(line):
            grid[y].append(Tree(char, x, y))

    best_view = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            tree = grid[y][x]
            tree_view = []
            for direction in direction_absolutes():
                trees_in_direction = 0
                x_comp = direction[0]
                y_comp = direction[1]
                while True:
                    if x + x_comp < 0 or y + y_comp < 0:
                        break
                    try:
                        comp_tree = grid[y + y_comp][x + x_comp]
                        trees_in_direction += 1
                        if tree.height <= comp_tree.height:
                            break
                    except IndexError:
                        break
                    x_comp += direction[0]
                    y_comp += direction[1]
                tree_view.append(trees_in_direction)
            if prod(tree_view) > best_view:
                best_view = prod(tree_view)
    return best_view


def main():
    with open("2022/Day_08/input.txt") as f:
        data = f.read()
    answer = compute1(data)
    print(answer)
    answer = compute2(data)
    print(answer)


@pytest.mark.parametrize("input_, expected", [
    ("""30373
25512
65332
33549
35390""", 21),
    ])
def test1(input_, expected):
    assert compute1(input_) == expected


@pytest.mark.parametrize("input_, expected", [
    ("""30373
25512
65332
33549
35390""", 8),
    ])
def test2(input_, expected):
    assert compute2(input_) == expected


if __name__ == "__main__":
    format_time(main)
