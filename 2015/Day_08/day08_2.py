import re

with open('day08.txt') as f:
    input_ = f.read().split('\n')
    
pattern = r'\\|"'

total = 0
for line in input_:
    ll = len(line)
    number = re.sub(pattern, "ll", line)
    total += len(number)+2 - ll
    print(line)
    print(number)
    print()
print(total)
