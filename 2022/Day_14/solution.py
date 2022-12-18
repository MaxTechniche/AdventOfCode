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

def parse(data):
    placed_rock = set()
    row_max = 0
    rock_paths = data.splitlines()
    for rock_path in rock_paths:
        rock_path = rock_path.split(" -> ")
        for i in range(len(rock_path) - 1):
            rock1 = tuple(map(int, rock_path[i].split(",")))
            rock2 = tuple(map(int, rock_path[i + 1].split(",")))
            row_max = max(row_max, rock1[1], rock2[1])
            if rock1[0] == rock2[0]:
                if rock1[1] < rock2[1]:
                    for j in range(rock1[1], rock2[1] + 1):
                        placed_rock.add((rock1[0], j))
                elif rock1[1] > rock2[1]:
                    for j in range(rock2[1], rock1[1] + 1):
                        placed_rock.add((rock1[0], j))
                else:
                    placed_rock.add(rock1)
            elif rock1[1] == rock2[1]:
                if rock1[0] < rock2[0]:
                    for j in range(rock1[0], rock2[0] + 1):
                        placed_rock.add((j, rock1[1]))
                elif rock1[0] > rock2[0]:
                    for j in range(rock2[0], rock1[0] + 1):
                        placed_rock.add((j, rock1[1]))
                else:
                    placed_rock.add(rock1)

    return row_max, placed_rock


def place_grain(row_max, placed_rock, sand):
    grain = [500, 0]
    while True:
        # print(grain)
        if grain[1] > row_max:
            return False, sand
        # Check directly below
        if (grain[0], grain[1] + 1) in placed_rock or (grain[0], grain[1] + 1) in sand:
            # Check left fill
            if (grain[0] - 1, grain[1] + 1) in placed_rock or (grain[0] - 1, grain[1] + 1) in sand:
                # Check right fill
                if (grain[0] + 1, grain[1] + 1) in placed_rock or (grain[0] + 1, grain[1] + 1) in sand:
                    sand.add(tuple(grain))
                    return True, sand
                else:
                    grain[0] += 1
            else:
                grain[0] -= 1
        grain[1] += 1
        

def place_grain2(row_max, placed_rock, sand):
    grain = [500, 0]
    while True:
        placed_rock.add((grain[0], row_max + 2))
        placed_rock.add((grain[0] - 1, row_max + 2))
        placed_rock.add((grain[0] + 1, row_max + 2))
        
        # Check directly below
        if (grain[0], grain[1] + 1) in placed_rock or (grain[0], grain[1] + 1) in sand:
            # Check left fill
            if (grain[0] - 1, grain[1] + 1) in placed_rock or (grain[0] - 1, grain[1] + 1) in sand:
                # Check right fill
                if (grain[0] + 1, grain[1] + 1) in placed_rock or (grain[0] + 1, grain[1] + 1) in sand:
                    if tuple(grain) in sand:
                        return False, sand
                    sand.add(tuple(grain))
                    return True, sand
                else:
                    grain[0] += 1
            else:
                grain[0] -= 1
        grain[1] += 1



def display(placed_rock, sand):
    x_min = min(placed_rock, key=lambda x: x[0])[0]
    y_min = min(placed_rock, key=lambda x: x[1])[1]
    x_max = max(placed_rock, key=lambda x: x[0])[0]
    y_max = max(placed_rock, key=lambda x: x[1])[1]
    
    size_x = x_max - x_min
    size_y = y_max - y_min + 3
    
    grid = [["."] * (size_x+1) for _ in range(size_y + 1)]
    
    
    for x, y in placed_rock:
        y += 3
        grid[y - y_min][x - x_min] = "#"
        
    for x, y in sand:
        y += 3
        grid[y - y_min][x - x_min] = "o"
        
    grid[0][500 - x_min] = "+"
    
    for row in grid:
        print("".join(row))
        
    with open("2022/Day_14/grid.txt", "w") as f:
        grid = [["."] * (x_max+1) for _ in range(y_max + 1)]
        for x, y in placed_rock:
            grid[y][x] = "#"
        for x, y in sand:
            grid[y][x] = "o"
        grid[0][500] = "+"
        for row in grid:
            f.write("".join(row) + "\n")


def compute1(data):
    row_max, placed_rock = parse(data)
    sand = set()
    while True:
        placed, sand = place_grain(row_max, placed_rock, sand)
        if placed is False:
            break
        
    # display(placed_rock, sand)
    return len(sand)


def compute2(data):
    row_max, placed_rock = parse(data)
    sand = set()
    while True:
        placed, sand = place_grain2(row_max, placed_rock, sand)
        if placed is False:
            break
        
    # display(placed_rock, sand)
    return len(sand)


def main():
    with open("2022/Day_14/input.txt") as f:
        data = f.read()
    answer = compute1(data)
    print(answer)
    answer = compute2(data)
    print(answer)


@pytest.mark.parametrize("input_, expected", [
    ("""498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9""", 24),
    ])
def test1(input_, expected):
    assert compute1(input_) == expected


@pytest.mark.parametrize("input_, expected", [
    ("""498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9""", 93),
    ])
def test2(input_, expected):
    assert compute2(input_) == expected


if __name__ == "__main__":
    format_time(main)


# ...o#ooo#.
# ..###ooo#.
# ....oooo#.
# .o.ooooo#.
# #####ooo#.