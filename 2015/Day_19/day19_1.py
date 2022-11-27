import re
from collections import defaultdict

replacements = defaultdict(list)

for line in open('AOC_2015\day19.txt'):
    a, b = re.match('(\w+) => (\w+)', line).groups()
    replacements[a].append(b)

with open('AOC_2015\day19 code.txt') as f:
    code = f.read()

class RList(list):
    def __init__(self, lst) -> None:
        super().__init__(lst)

    def replace(self, index, item):
        new_lst = self[:]
        del new_lst[index]
        new_lst.insert(index, item)
        return new_lst

pattern = '([A-Z][a-z]*|[A-Z])'

code_sets = set()

g = RList(re.findall(pattern, code))


for mol in range(len(g)):
    for replacement in replacements[g[mol]]:
        code_sets.add(''.join(g.replace(mol, replacement)))
        
print(len(code_sets))

