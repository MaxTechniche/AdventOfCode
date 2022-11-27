import re
import json

with open('day12.txt') as f:
    input_ = f.read()
    
total = 0
pattern = r'-?\d+'

for number in re.findall(pattern, input_):
    total += int(number)

input_ = json.loads(input_)
print(total)

remaining_objects = [input_]

total = 0

while remaining_objects:
    x = remaining_objects.pop()
    if type(x) == dict:
        if 'red' in x.values():
            continue
        if 'red' in x:
            continue
        for key, value in x.items():
            remaining_objects.append(key)
            remaining_objects.append(value)
    elif type(x) == list:
        remaining_objects.extend(x)
    elif type(x) == int:
        total += x
    else:
        continue
        
            
print(total)
