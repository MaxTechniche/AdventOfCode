import re

with open('day12.txt') as f:
    input_ = f.read()
    
total = 0
pattern = r'-?\d+'

for number in re.findall(pattern, input_):
    total += int(number)

print(total)