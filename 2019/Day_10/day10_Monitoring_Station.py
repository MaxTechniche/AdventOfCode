from math import gcd
from collections import defaultdict
from copy import deepcopy

print(gcd(0, 0))


def translatePoint(origin, point):
    return (point[0] - origin[0], point[1] - origin[1])


def gcFactored(point):
    f = gcd(point[0], point[1])
    return (point[0]//f if f != 0 else 0, point[1]//f if f != 0 else 0)

def gcm(numbers):
    numbers = [abs(x) for x in numbers]
    numbers.sort()
    numbers.reverse()
    multiple = numbers[0]
    while True:
        for num in numbers:
            if multiple % num != 0:
                multiple *= num
        else:
            return multiple

with open('day10_input.txt', 'r') as f:
    input_ = f.read().split('\n')


gjsdl = 21416915520

asteroid_list = []
for x in range(len(input_)):
    for y in range(len(input_[x])):
        if input_[x][y] == '#':
            asteroid_list.append((x, y))


print(gcm([x for x in range(1, 25)]))
best_asteroid_dict = None
most_asteroids = 0
for asteroid_origin in range(len(asteroid_list)):
    current_biggest_x = 0
    current_biggest_y = 0
    current_test = []
    asteroid_dict = defaultdict()
    for testing_asteroid in range(len(asteroid_list)):
        if asteroid_origin == testing_asteroid:
            continue
        factored = gcFactored(translatePoint(
            asteroid_list[asteroid_origin], asteroid_list[testing_asteroid]))
        if factored in asteroid_dict:
            asteroid_dict[factored].append(asteroid_list[testing_asteroid])
        else:
            asteroid_dict[factored] = [asteroid_list[testing_asteroid]]
    if len(asteroid_dict) > most_asteroids:
        best_asteroid_dict = deepcopy(asteroid_dict)
        most_asteroids = len(asteroid_dict)
        best_position = asteroid_list[testing_asteroid]

longest_x = 600
longest_y = 600
print(best_position)
print(most_asteroids)
x = best_position[0]
y = 0
destroyed = 0
print(x, y)
print(longest_x)
x_dir = True
y_dir = False
x_low = 0
y_low = 0
min_repeat = False
min_repeat_count = 0
val = 1
while len(best_asteroid_dict):
    factored = gcFactored(translatePoint(best_position, (x, y)))
    if factored in best_asteroid_dict:
        print(len(best_asteroid_dict))
        destroyed += 1
        if destroyed == 200:
            print((x, y))
        del best_asteroid_dict[factored]
    if min_repeat_count == 3:
        min_repeat = True
        min_repeat_count = 0
    else:
        if x == 600:
            min_repeat_count += 1
    if min_repeat:
        x_low += 1
    if x == x_low and y == y_low:
        x_dir = True
        y_dir = False
        val = -val
    elif x == longest_x and y == longest_y:
        x_dir = True
        y_dir = False
        val = -val
    elif x == longest_x and y == y_low:
        x_dir = False
        y_dir = True
    elif x == x_low and y == longest_y:
        x_dir = False
        y_dir = True

    if x_dir:
        x += val
    else:
        y += val
