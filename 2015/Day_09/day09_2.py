"""
import random

with open('day09.txt') as f:
    input_ = f.read().split('\n')
    
input_ = [x.split(' = ')[::-1] for x in input_]
input_ = [[int(x[0]), x[1].split(' to ')] for x in input_]

input_.sort(reverse=True)
print(*input_, sep='\n')

total = 0

for x in range(len(input_)):
    used_cities = input_[x][1]
    used_distances = [input_[x][0]]
    change = True
    while change:
        for d in input_:
            if d[1][0] in (used_cities[0], used_cities[-1]):
                if d[1][1] not in used_cities:
                    if d[1][0] == used_cities[0]:
                        used_cities.insert(0, d[1][1])
                        used_distances.insert(0, d[0])
                        break
                    elif d[1][0] == used_cities[-1]:
                        used_cities.append(d[1][1])
                        used_distances.append(d[0])
                        break
            elif d[1][1] in (used_cities[0], used_cities[-1]):
                if d[1][0] not in used_cities:
                    if d[1][1] == used_cities[0]:
                        used_cities.insert(0, d[1][0])
                        used_distances.insert(0, d[0])
                        break
                    elif d[1][1] == used_cities[-1]:
                        used_cities.append(d[1][0])
                        used_distances.append(d[0])
                        break
        else:
            change = False
            
    print(sum(used_distances), used_distances)
    print(used_cities)
            
    total = max(total, sum(used_distances))
print(total)
"""
import sys
from itertools import permutations

places = set()
distances = dict()
for line in open('day09.txt'):
    (source, _, dest, _, distance) = line.split()
    places.add(source)
    places.add(dest)
    distances.setdefault(source, dict())[dest] = int(distance)
    distances.setdefault(dest, dict())[source] = int(distance)

shortest = sys.maxsize
longest = 0
for items in permutations(places):
    dist = sum(map(lambda x, y: distances[x][y], items[:-1], items[1:]))
    shortest = min(shortest, dist)
    longest = max(longest, dist)

print("shortest: %d" % (shortest))
print("longest: %d" % (longest))