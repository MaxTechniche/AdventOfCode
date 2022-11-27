import re

with open('day08.txt') as f:
    input_ = f.read().split('\n')
    
pattern = r'\\(x..|"|\\)'

total = 0
for line in input_:
    total += len(line)
    line = re.sub(pattern, "_", line[1:-1])
    total -= len(line)
print(total)