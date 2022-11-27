import re
from itertools import permutations
from functools import reduce

path_to_file = 'J:\Tech Stuff\Documents\My Program Codes\Advent Of Code\AOC_2015\day15.txt'

ingredients = dict()
for line in open(path_to_file):
    i = re.search('(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)', line)
    n = i.group(1)
    ingredients[n] = list(map(int, i.group(2, 3, 4, 5)))

print(ingredients)

def multiply(a, b):
    return a*b

total = 0
x = list(range(101))
for a in permutations(x, len(ingredients)):
    if sum(a) != 100:
        continue
    s = zip(a, (ingredients[i] for i in ingredients))
    s = [[z[0] * z[1][y] for y in range(len(z[1]))] for z in s]
    s = zip(*s)
    s = [sum(t) for t in s]
    if any(e <= 0 for e in s):
        continue
    s = reduce(multiply, s)
    total = max(total, s)
    
print(total)