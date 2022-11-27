from time import time
from pprint import pprint


class Cave:
    def __init__(self, value, connected_caves=None):
        self.value = value
        if connected_caves:
            self.connected_caves = connected_caves
        else:
            self.connected_caves = []


class Paths:
    paths = 0

    @classmethod
    def add_path(self):
        Paths.paths += 1

    @classmethod
    def get_total_paths(self):
        return Paths.paths


def display_connections(caves):
    for cave, connections in caves.items():
        connections = [x.value for x in connections.connected_caves]
        pprint((cave, connections))


def find_paths(current_cave, visited_caves, part2=False, lowercase_twice=False):
    if current_cave.value in visited_caves and current_cave.value.islower():
        lowercase_twice = True
    visited_caves.append(current_cave.value)

    for next_cave in current_cave.connected_caves:
        if next_cave.value == 'end':
            Paths.add_path()
            continue
        if next_cave.value == 'start':
            continue

        if next_cave.value in visited_caves and next_cave.value.islower():
            if part2:
                if lowercase_twice:
                    continue
            else:
                continue

        find_paths(next_cave, visited_caves, part2, lowercase_twice)
    visited_caves.pop()
    lowercase_twice = False


def main():
    t1 = time()

    with open("2021/Day_12/input") as f:
        connections = f.read().splitlines()

    caves = {}

    for connection in connections:
        l, r = connection.split('-')
        if l in caves:
            if r in caves:
                caves[r].connected_caves.append(caves[l])
                caves[l].connected_caves.append(caves[r])
            else:
                caves[r] = Cave(r, [caves[l]])
                caves[l].connected_caves.append(caves[r])
        elif r in caves:
            if l in caves:
                caves[l].connected_caves.append(caves[r])
                caves[r].connected_caves.append(caves[l])
            else:
                caves[l] = Cave(l, [caves[r]])
                caves[r].connected_caves.append(caves[l])
        else:
            caves[l] = Cave(l)
            caves[r] = Cave(r)
            caves[l].connected_caves.append(caves[r])
            caves[r].connected_caves.append(caves[l])

    # display_connections(caves)

    visited_caves = []
    find_paths(caves['start'], visited_caves, False)

    print(Paths.get_total_paths())

    print("Time:", time() - t1)


main()
