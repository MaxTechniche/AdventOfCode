import re
from collections import defaultdict
from itertools import permutations

name_connections = defaultdict(dict)
for line in open('day13.txt'):
    found = re.search('(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+)\.', line)
    name1, option, mutual_happiness, name2 = found.group(1, 2, 3, 4)
    name_connections[name1][name2] = int(mutual_happiness) * (-1 if (option == 'lose') else 1)
    
def find_max_happiness(name_connections):
    maximum_happiness = 0
    for seating in permutations(name_connections):
        happiness = sum(name_connections[a][b] + name_connections[b][a] for a, b in zip(seating[:-1], seating[1:]))
        happiness += name_connections[seating[0]][seating[-1]] + name_connections[seating[-1]][seating[0]]
        maximum_happiness = max(maximum_happiness, happiness)
    return maximum_happiness

print(find_max_happiness(name_connections))

for name in list(name_connections):
    name_connections[name]['me'] = 0
    name_connections['me'][name] = 0
    
print(find_max_happiness(name_connections))
