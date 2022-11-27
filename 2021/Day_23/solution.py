from time import time, sleep
from cProfile import run
from timeit import timeit
from pprint import pprint


INPUT_LINES = """#############
#...........#
###B#C#C#B###
  #D#D#A#A#
  #########"""

PART_2_INPUT_LINES = """#############
#...........#
###B#C#C#B###
  #D#C#B#A#
  #D#B#A#C#
  #D#D#A#A#
  #########"""

SAMPLE_LINES = """#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########"""

PART_2_SAMPLE_LINES = """#############
#...........#
###B#C#B#D###
  #D#C#B#A#
  #D#B#A#C#
  #A#D#C#A#
  #########"""

LINES = [list(line) for line in PART_2_INPUT_LINES.splitlines()]

LOWEST_COST = float('inf')
COSTS = {
    'A': 1,
    'B': 10,
    'C': 100,
    'D': 1000
}
AM_ROOMS = {
    'A': 3,
    'B': 5,
    'C': 7,
    'D': 9
}
ILLEGAL_SPOTS = set([(1, 3), (1, 5), (1, 7), (1, 9)])
BOARD_POSITIONS = set()

NUM_LINES = len(LINES)
ROW = 0
COLUMN = 1
SETS = {}


for x in range(NUM_LINES):
    for y in range(len(LINES[x])):
        if LINES[x][y] in '.ABCD':
            BOARD_POSITIONS.add((x, y))


def display(ams):
    layout = """#############
#...........#
###.#.#.#.###
  #.#.#.#.#
  #########"""
    if len(ams) > 8:
        layout = """#############
#...........#
###.#.#.#.###
  #.#.#.#.#
  #.#.#.#.#
  #.#.#.#.#
  #########"""
    layout = [list(line) for line in layout.splitlines()]
    for am in ams:
        layout[am[0]][am[1]] = ams[am]

    for row in layout:
        print(''.join(row))


def store(ams):
    layout = """#############
#...........#
###.#.#.#.###
  #.#.#.#.#
  #.#.#.#.#
  #.#.#.#.#
  #########"""
    
    layout = [list(line) for line in layout.splitlines()]
    for am in ams:
        layout[am[0]][am[1]] = ams[am]

    grid = ''.join(layout[0])
    for row in layout[1:]:
        grid += '\n' + ''.join(row)

    return grid


def path_is_clear(cp, np, ams):
    if cp[ROW] > 1:
        for x in range(1, cp[ROW]):
            if (x, cp[COLUMN]) in ams:
                return False

    if np[ROW] > 1:
        for x in range(1, np[ROW]+1):
            if (x, np[COLUMN]) == cp:
                continue
            if (x, np[COLUMN]) in ams:
                return False

    if np[COLUMN] < cp[COLUMN]:
        for y in range(np[COLUMN], cp[COLUMN]):
            if (1, y) in ams:
                return False

    elif cp[COLUMN] < np[COLUMN]:
        for y in range(cp[COLUMN]+1, np[COLUMN]+1):
            if (1, y) in ams:
                return False

    return True


def legal_position(cp, np, ams):
    if np == cp:
        return False
    # Can only move into a room of its type
    if np[ROW] != 1 and np[COLUMN] != AM_ROOMS[ams[cp]]:
        return False
    # Cannot block a room
    if tuple(np) in ILLEGAL_SPOTS:
        return False
    # Can only move into or out of a room
    if cp[ROW] == np[ROW] == 1 or cp[COLUMN] == np[COLUMN]:
        return False
    # Cannot block a different letter when entering its room
    for x in range(np[ROW], NUM_LINES):
        if (x, np[COLUMN]) in ams:
            if ams[(x, np[COLUMN])] in [ams[cp], '#']:
                continue
            return False
    return True


def in_own_room(am, ams):
    if am[1] == AM_ROOMS[ams[am]]:
        return True

    return False


def locked_in(cp, ams):
    if not in_own_room(cp, ams):
        return False

    for x in range(cp[0], NUM_LINES):
        if (x, cp[1]) in ams and ams[(x, cp[1])] not in [ams[cp], '#']:
            return False

    return True


def move(am, np, ams):
    cost = 0
    if np[0] != 1:
        cost += abs(np[0] - 1)
    if am[0] != 1:
        cost += abs(am[0] - 1)
    cost += abs(am[1] - np[1])
    return cost * COSTS[ams[np]]


def all_in(ams):
    # for letter, room in zip(list('ABCD'), AM_ROOMS.values()):
    for pos, letter in ams.items():
        if AM_ROOMS[letter] != pos[1]:
            return False

    return True


def solve(ams, cost, memo):
    if store(ams) in memo:
        if cost >= memo[store(ams)]:
            return

    memo[store(ams)] = cost
    global LOWEST_COST
    # display(ams)
    # sleep(.25)
    # print('')
    # if cost > LOWEST_COST:
    #     return
    if all_in(ams):
        print(LOWEST_COST)
        if cost < LOWEST_COST:
            # for m, c in zip(move_set, cost_set):
            #     print(c)
            #     print(*m, sep='\n')
            #     print()
            # display(ams)
            print(cost)
            LOWEST_COST = cost
        return
    for cp in list(ams):
        if locked_in(cp, ams):
            continue
        for position in BOARD_POSITIONS:

            if position == cp:
                continue
            # Can only move into a room of its type
            if position[ROW] != 1 and position[COLUMN] != AM_ROOMS[ams[cp]]:
                continue
            # Cannot block a room
            if tuple(position) in ILLEGAL_SPOTS:
                continue
            # Can only move into or out of a room
            if cp[ROW] == position[ROW] == 1 or cp[COLUMN] == position[COLUMN]:
                continue
            # Cannot block a different letter when entering its room
            okay = True
            for x in range(position[ROW], NUM_LINES):
                if (x, position[COLUMN]) in ams:
                    if ams[(x, position[COLUMN])] in [ams[cp], '#']:
                        continue
                    okay = False
                    break
    
            if not okay:
                continue
            if path_is_clear(cp, position, ams):
                old_pos = cp
                letter = ams[cp]
                del ams[old_pos]
                ams[position] = letter
                solve(ams, cost+move(cp, position, ams), memo)
                del ams[position]
                ams[old_pos] = letter


def main():
    t1 = time()

    ams = {}
    layout = LINES
    for i, v in enumerate(layout):
        for j, k in enumerate(v):
            if k in 'ABCD':
                ams[(i, j)] = k

    memo = {}

    solve(ams, 0, memo)
    # display(layout)

    print("Time:", time() - t1)


# run("main()")
main()
