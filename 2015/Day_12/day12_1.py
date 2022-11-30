import re

with open("input.txt") as f:
    input_ = f.read()
    
total = 0
pattern = r'-?\d+'

for number in re.findall(pattern, input_):
    total += int(number)

print(total)