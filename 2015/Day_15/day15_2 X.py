import re
from itertools import permutations
from functools import reduce
from operator import mul

path_to_file = 'J:\Tech Stuff\Documents\My Program Codes\Advent Of Code\AOC_2015\day15.txt'

ingredients = dict()
for line in open(path_to_file):
    i = re.search('(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)', line)
    n = i.group(1)
    ingredients[n] = list(map(int, i.group(2, 3, 4, 5, 6)))

total = 0
x = list(range(101))
for a in permutations(x, len(ingredients)):
    if sum(a) != 100:
        continue
    s = list(zip(a, (ingredients[i] for i in ingredients)))
    s = [[z[0] * z[1][y] for y in range(len(z[1]))] for z in s]
    s = list(zip(*s))
    s = [sum(t) for t in s]
    if s[-1] != 500:
        continue
    if any(e <= 0 for e in s):
        continue
    cals = s[-1]
    s = reduce(mul, s[:-1])
    total = max(total, s)
    
print(total)

"""
import re
import numpy as np

from functools import reduce
from operator import mul

m = []
for line in open('J:\Tech Stuff\Documents\My Program Codes\Advent Of Code\AOC_2015\day15.txt'):
    c, d, f, t, cal = map(int, re.findall('-?\d+', line))
    m.append([c, d, f, t, cal])
m = np.array(m)

def min_zero_sum(*ns):
    return max(0, sum(ns))

scores = [(reduce(mul, map(min_zero_sum, 
                          *map(mul, [i, j, k, l], m[:, :-1]))),
           sum(map(mul, [i, j, k, l], m[:, -1])))
          for i in range(101) 
          for j in range(0, 101-i) 
          for k in range(0, 101-j-i) 
          for l in [100 - i - j - k]]
# Part 1
print(max(s[0] for s in scores))

# Part 2
print(max(s[0] for s in scores if s[1] == 500)) 
"""