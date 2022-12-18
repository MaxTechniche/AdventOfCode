import pytest
from string import ascii_lowercase
import sys

sys.setrecursionlimit(7000)

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


alpha = {v: i for i, v in enumerate(ascii_lowercase)}
alpha["S"] = 19
alpha["Z"] = 26


def directions():
    return ((0, 1), (1, 0), (-1, 0), (0, -1))


def get_neighbors(cell):
    row, col = cell
    for direction in directions():
        yield direction[0] + row, direction[1] + col


def bfs(cell, node_list, target="E"):
    visited = set()
    queue = [cell]
    visited.add(cell)
    x = 0
    while x < len(queue):
        current_cell = node_list[queue[x]]
        steps = current_cell.min_steps
        for neighbor in get_neighbors(current_cell.coords):
            if neighbor not in node_list:
                continue
            if neighbor in visited:
                continue

            neighbor = node_list[neighbor]

            if target == "E":
                if current_cell.stepable(neighbor):
                    neighbor.min_steps = min(neighbor.min_steps, steps + 1)
                else:
                    continue

                if neighbor.value == "E":
                    return neighbor.min_steps

            elif target == "a":
                if neighbor.stepable(current_cell):
                    neighbor.min_steps = min(neighbor.min_steps, steps + 1)
                else:
                    continue

                if neighbor.value == "a":
                    return neighbor.min_steps

            visited.add(neighbor.coords)
            queue.append(neighbor.coords)
        x += 1
    return queue


class Node:
    def __init__(self, step, coords):
        if step == "E":
            self.step: int = alpha["z"]
        elif step == "S":
            self.step: int = alpha["a"]
        else:
            self.step: int = alpha[step]
        self.coords: tuple[int, int] = coords
        self.neighbors: list = []
        self.value: str = step
        self._min_steps: float = float("inf")
        
    @property
    def min_steps(self):
        return self._min_steps
    
    @min_steps.setter
    def min_steps(self, value):
        self._min_steps = value

    def set_neighbors(self, node_list):
        for neighbor in get_neighbors(self.coords):
            if neighbor in node_list:
                self.neighbors.append(node_list[neighbor])
            else:
                self.neighbors.append(None)

    def stepable(self, node: "Node"):
        if node is None:
            return False
        if self.step + 1 >= node.step:
            return True
        return False

    def __repr__(self) -> str:
        return f"Node({self.value}, {self.step}, {self.coords})"


MIN_STEPS = {"min": float("inf"), "calls": 0}


def solve(node, steps=0, visited=None):
    MIN_STEPS["calls"] += 1
    # print(MIN_STEPS["calls"])
    if visited is None:
        visited = set()
    visited.add(node)
    if node.value == "E":
        if steps < MIN_STEPS["min"]:
            MIN_STEPS["min"] = steps
            print(MIN_STEPS["min"])
        return
    # print(node.value, node.step, node.coords, len(visited))
    for neighbor in node.neighbors:
        if neighbor not in visited and node.stepable(neighbor):
            solve(neighbor, steps + 1, visited)
            visited.remove(neighbor)


def get_start_end_and_node_list(data):
    node_list = {}
    start = end = None
    for r, row in enumerate(data.splitlines()):
        for c, step in enumerate(row.strip()):
            node_list[(r, c)] = Node(step, (r, c))
            if step == "S":
                start = node_list[(r, c)]
            elif step == "E":
                end = node_list[(r, c)]

    for node in node_list.values():
        node.set_neighbors(node_list)

    return start, end, node_list


def compute1(data):
    start, end, node_list = get_start_end_and_node_list(data)
    start.min_steps = 0
    answer = bfs(start.coords, node_list, "E")
    return answer


def compute2(data):
    start, end, node_list = get_start_end_and_node_list(data)
    end.min_steps = 0
    answer = bfs(end.coords, node_list, "a")
    return answer


def main():
    with open("2022/Day_12/input.txt") as f:
        data = f.read()
    answer = compute1(data)
    print(answer)
    answer = compute2(data)
    print(answer)


@pytest.mark.parametrize(
    "input_, expected",
    [
        (
            """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi""",
            31,
        ),
    ],
)
def test1(input_, expected):
    assert compute1(input_) == expected


@pytest.mark.parametrize(
    "input_, expected",
    [
        (
            """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi""",
            29,
        ),
    ],
)
def test2(input_, expected):
    assert compute2(input_) == expected


if __name__ == "__main__":
    format_time(main)
