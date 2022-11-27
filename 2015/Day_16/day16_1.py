import re
from collections import defaultdict

sue = {}

for line in open('AOC_2015\day16 tt.txt'):
    a, b = re.search('(\w+): (\d+)', line).groups()
    sue[a] = int(b)

for line in open('AOC_2015\day16.txt'):
    s = re.search('Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)', line)
    check = {}
    for x in range(2, len(s.groups()), 2):
        check[s.group(x)] = int(s.group(x+1))
    if check.items() <= sue.items():
        print(line)
