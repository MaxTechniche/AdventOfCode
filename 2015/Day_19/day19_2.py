import re
from collections import defaultdict
from typing import Pattern

replacements = dict()

for line in open('AOC_2015\day19.txt'):
    a, b = re.match('(\w+) => (\w+)', line).groups()
    replacements[b] = a

with open('AOC_2015\day19 code.txt') as f:
    code = f.read().split('\n')[0]

def replacements_adds(long_string, pattern, replacements):
    g = re.findall(pattern[2:-3], long_string)
    r = ''
    for _g in g:
        r += replacements[_g]
    return r

pattern = '|'.join([_w for _w in sorted(replacements.keys(), key=len, reverse=True)])
pattern = '((' + pattern + ')+)'

p_code_sets = {code}

steps = 0
running = True
r = True

while running:
    steps += 1
    code_sets = set()
    for c in p_code_sets:
        g = re.findall(pattern, c)
        if not g:
            running = False
            break
        for match in g:
            cc = c[:]
            code_sets.add(cc.replace(match[0], replacements_adds(match[0], pattern, replacements)))
        
    p_code_sets = code_sets.copy()
    print(steps)
    print(len(p_code_sets))
    print()
    
print(steps)